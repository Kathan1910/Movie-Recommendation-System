from setuptools import setup

with open("README.md","r",encoding="utf-8") as fh:
    long_description = fh.read()
    
AUTHOR_NAME = 'KATHAN PATEL'
SRC_REPO = 'src'
LIST_OF_REQUIREMENT = ['streamlit']

setup(
    name = SRC_REPO,
    version = '0.0.1',
    author = AUTHOR_NAME,
    author_email = 'kathanpatel1910@gmail.com',
    description = 'A small example package for movie recommendation',
    long_description= long_description,
    long_description_content_type = 'text/markdown',
    package = [SRC_REPO],
    python_version = '>=3.7',
    install_requires = LIST_OF_REQUIREMENT,
)