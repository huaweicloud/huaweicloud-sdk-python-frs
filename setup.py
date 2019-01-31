# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name = "frs-python-sdk",
    version = "2.0.0",
    packages = find_packages(),
    zip_safe = False,
    description = "FRS Python SDK",
    license = "Apache2.0",
    keywords = ('frs', 'sdk', 'huawei', 'cloud'),
    platforms = "Independent",
    url = "https://support.huaweicloud.com/face/index.html",
    install_requires = [
        'requests>2.0'
    ]
)
