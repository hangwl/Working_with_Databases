from setuptools import find_packages, setup

setup(
    name="demo_project",
    packages=find_packages(exclude=["demo_project_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagit", "pytest", "psycopg2", "pandas", "matplotlib", "dagster_duckdb_pandas"]},
)
