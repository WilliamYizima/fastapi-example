from setuptools import setup, find_packages


def read(filename):
    return [
        req.strip() 
        for req 
        in open(filename).readlines()
        ]

setup(
    name="example",
    version="0.1.0",
    description="example app",
    packages=find_packages(),
    include_package_data=True,
    install_requires=read("requirements.txt"),
    extras_require={
        "dev": read("requirements-dev.txt")
    }
)