from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="download-cleaner",
    version="1.0.0",
    author="rijtim1",
    description="A Python package to clean and organize your downloads folder",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Rijtim1/download-cleaner",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "tqdm"
    ],
    entry_points={
        'console_scripts': [
            'download-cleaner=download_cleaner.clean:main',
        ],
    },
)