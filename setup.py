import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="graphscii",
    version="0.0.1",
    author="Agastya Pawate",
    author_email="apawate739@student.fuhsd.org",
    description="A Python library for making graphics using ASCII characters.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/apawate/graphscii",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
