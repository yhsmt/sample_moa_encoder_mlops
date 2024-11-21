import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="data-import",
    version="0.0.1",
    description="Lambda function of LA Data Import",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="author",
    package_dir={"": "."},
    packages=setuptools.find_packages(where="app"),
    install_requires=["boto3"],
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",
        "Typing :: Typed",
    ],
)
