

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="001-setup-tools-level1", # Replace with your own username
    version="0.0.1",
    author="Saket Verma",
    author_email="saket.verma@test.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/saket1471/001-setup-tools-level1",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['000-setup-tools-base==0.0.1'],
    dependency_links=['https://github.com/saket1471/000-setup-tools-base/blob/master/dist/000-setup-tools-base-0.0.1.zip'],
)
