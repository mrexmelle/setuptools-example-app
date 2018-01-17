
#!/bin/python

from setuptools import setup, find_packages

setup(
	name="setuptools-example-hello",
	version="1.0",
	packages=find_packages(),
	url="https://github.com/mrexmelle/setuptools-example-hello",
	entry_points={
        'console_scripts': [
            'setuptools-hello = hello.main:main',
        ]}
)

