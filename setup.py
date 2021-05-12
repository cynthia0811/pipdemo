#!/usr/bin/python
# encoding: utf-8



from setuptools import setup, find_packages
 
setup(
    name="pipdemo",
    version="0.1",
    license="MIT Licence",
 
    url="https://github.com/cynthia0811/pipdemo.git",
    author="lfyin",
    author_email="13814538110@163.com",
 
    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=[]
)