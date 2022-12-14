import os

from setuptools import setup,find_packages

here = os.path.abspath(os.path.dirname(__file__))

VERSION = "0.0.4"

with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="chrome-spider",
    version=VERSION,
    url="https://github.com/gaianote/chrome-spider",
    author="gaianote",
    author_email="gaianote311@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=True,
    packages=find_packages(),
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
    ],
    entry_points={
        "console_scripts": [
            "chrome-spider = chrome_spider.app:main"
        ]
    },
    install_requires=[
        "webdriver-manager >= 3.8.3",
        "selenium >= 4.4.3"
    ],
    extras_require={
        "dev": [
        ]
    },
)
