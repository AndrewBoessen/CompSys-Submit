import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "CompSys-Submit",
    version = "0.0.1",
    author = "Andrew Boessen",
    author_email = "boessena@bc.edu",
    description = "Tool to automate submitting assignment for Computer Systems course at BC",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/AndrewBoessen/CompSys-Submit",
    project_urls = {
        "Bug Tracker": "https://github.com/AndrewBoessen/CompSys-Submit/issues",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    python_requires = ">=3.8"
)
