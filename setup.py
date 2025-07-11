from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ArchiveExtractorModule",
    version="1.0.0.0",
    author="WNS",
    author_email="wnsoff@yandex.ru",
    description="Python library for extracting ZIP, RAR and 7z archives with comic book formats support",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wns444/ArchiveExtractor.git",
    packages=find_packages(),
    install_requires=[
        'rarfile>=4.0',
        'py7zr>=0.20.0',
    ],
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
    python_requires='>=3.8',
    keywords='archive zip rar 7z extract cbr cb7 utility',
    project_urls={
        "Bug Tracker": "https://github.com/wns444/ArchiveExtractor/issues",
        "Documentation": "https://github.com/wns444/ArchiveExtractor/wiki",
        "Source Code": "https://github.com/wns444/ArchiveExtractor",
    },
)