# Querying Data through Python

Querying data through Python depends on the type of data source we are working with.

## Relational Databases

- Python Database API modules:
  - `sqlite3`: builtin module for SQLite
  - `psycopg2`: PostgreSQL
  - `mysql-connector-python`: MySQL
- Object-Relational Mappers (ORMs):
  - `sqlalchemy`: provides a higher-level abstraction to interact with databases
- Pandas Library: 
  - `pandas` is a popular python data manipulation and analysis library

## NoSQL Databases

Most NoSQL databases provide official Python clients that provide APIs to query and manipulate data.
- `pymongo`: MongoDB provides an on-disk unstructured database.
- `redispy`: Redios may be used in combination with MongoDB as a caching layer, or for performing real-time analytics.

## Web APIs

- `requests`: Library used to send HTTP requests to web APIs and retrieve data which is usually in JSON or XML format parsed through Python's builtin `json` or `xml` modules.

## Web Scraping

- `bs4`: `BeautifulSoup` allows us to extract data from HTML and XML documents by traversing the document's structure and querying elements based on tags, classes, or other attributes.
- `selenium`: Often used if a website relies on JavaScript or requires user interaction. Selenium can be used to automate web browser actions and retrieve data.