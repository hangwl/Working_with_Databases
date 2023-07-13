import base64
from io import BytesIO

import matplotlib.pyplot as plt
import pandas as pd
import requests
from bs4 import BeautifulSoup
import csv
from sqlalchemy import create_engine

from dagster import (
    AssetKey,
    DagsterInstance,
    MetadataValue,
    Output,
    asset,
    get_dagster_logger,
)

@asset
def pol_data():
    logger = get_dagster_logger()

    url = 'https://boards.4chan.org/pol/catalog.json'
    response = requests.get(url)
    response = response.json()

    data = []

    for items in response:
        page = items['page']
        threads = items['threads']
        for thread in threads:
            keys_to_extract = ['no', 'id', 'sub', 'com', 'replies', 'time', 'last_modified']
            thread_data = {key: thread.get(key) for key in keys_to_extract}
            data.append(thread_data)

        if len(data) % 10 == 0:
            logger.info(f"Got {len(data)} threads so far.")

    df = pd.DataFrame(data)
    df.fillna('', inplace=True)
    df['subcom'] = df['sub'] + ' ' + df['com']
    df = df[['no', 'id', 'subcom', 'replies', 'time', 'last_modified']]
    
    def extract_text(subcom):
        soup = BeautifulSoup(subcom, 'html.parser')
        extracted_text = soup.get_text()
        return extracted_text

    df['extracted_text'] = df['subcom'].apply(extract_text)
    cols = ['no', 'id', 'extracted_text', 'replies', 'time', 'last_modified']
    df = df[cols].sort_values(by='replies', ascending=False)

    return Output(
        value=df,
        metadata={
            "num_records": len(df),
            "preview": MetadataValue.md(df.head().to_markdown()),
        }
    )

@asset(
    non_argument_deps={"stopwords_csv"},  # Addition: added the dependency
)
def most_frequent_words(pol_data):
    with open("data/stopwords.csv", "r") as f:
        stopwords = {row[0] for row in csv.reader(f)}

    # loop through the titles and count the frequency of each word
    word_counts = {}
    for raw_text in pol_data["extracted_text"]:
        text = raw_text.lower()
        for word in text.split():
            cleaned_word = word.strip(".,-!?:;()[]'\"-")
            if cleaned_word not in stopwords and len(cleaned_word) > 0:
                word_counts[cleaned_word] = word_counts.get(cleaned_word, 0) + 1

    # Get the top 25 most frequent words
    top_words = {
        pair[0]: pair[1]
        for pair in sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:25]
    }

    # Make a bar chart of the top 25 words
    plt.figure(figsize=(10, 6))
    plt.bar(top_words.keys(), top_words.values())
    plt.xticks(rotation=45, ha="right")
    plt.title("Top 25 Words in /pol/")
    plt.tight_layout()

    # Convert the image to a saveable format
    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    image_data = base64.b64encode(buffer.getvalue())

    # Convert the image to Markdown to preview it within Dagster
    md_content = f"![img](data:image/png;base64,{image_data.decode()})"

    # Attach the Markdown content as metadata to the asset
    return Output(
        value=top_words,
        metadata={"plot": MetadataValue.md(md_content)},
    )

@asset
def update_sql_table(pol_data):
    connection_string = 'postgresql://postgres:password@localhost:5432/threads'
    engine = create_engine(connection_string)
    table_name = 'pol'
    pol_data.to_sql(name=table_name, con=engine, if_exists='replace', index=False)
    engine.dispose()