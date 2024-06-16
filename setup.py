from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="tocker",
    version="0.0.1",
    author="ropali",
    author_email="ropali68@example.com",
    description="A TUI for docker",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ropali/tocker",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
)
