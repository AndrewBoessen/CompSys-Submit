import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

this = os.path.dirname(os.path.realpath(__file__))


def read(name):
    with open(os.path.join(this, name)) as f:
        return f.read()

setuptools.setup(
    name = "cs-submit",
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
    packages = ["src/cs-submit"]
    install_requires = read("requirements.txt"),
    scripts = ["bin/cs-submit"]
    python_requires = ">=3.x"
)
