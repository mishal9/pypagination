import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pypagination",
    version="0.0.1",
    author="Mishal Shah",
    author_email="mshah31@asu.edu",
    description="A small library to paginate through json objects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mishal9/pypagination/issues",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)