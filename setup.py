#!/usr/bin/env python

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="margin_talib_service",
    version="0.0.1",
    author="Margin UG",
    author_email="contact@margin.io",
    description="Margin Strategy Editor SDK",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MarginOpenSource/strategy-sdk",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["rpyc", "TA-Lib"],
    entry_points={
        'console_scripts': [
            'margin-talib-service = margin_talib_service.service:main'
        ]
    },
    python_requires='>=3.5',
)
