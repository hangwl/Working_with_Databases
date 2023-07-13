from setuptools import find_packages, setup

setup(
    name="project_1",
    packages=find_packages(exclude=["project_1_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagit", "pytest"]},
)
