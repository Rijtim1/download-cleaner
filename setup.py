from setuptools import setup, find_packages

setup(
    name="download-cleaner",
    version="1.0.0",
    description="A Python package to clean and organize your downloads folder",
    packages=find_packages(),
    install_requires=[
        "tqdm",
        "shutil"
    ]
)