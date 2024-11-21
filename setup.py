import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="cdk-base",
    version="0.0.1",
    description="CDK Template Project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="author",
    package_dir={"": "app"},
    packages=setuptools.find_packages(where="app"),
    install_requires=[
        "aws-cdk-lib",
        "constructs",
    ],
    python_requires=">=3.12",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",
        "Typing :: Typed",
    ],
)
