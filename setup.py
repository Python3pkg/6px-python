from distutils.core import setup
import os

setup(
	name='6px',
	version='0.0.8',
	author='6px',
	author_email='ops@6px.io',
	packages=['_6px'],
	url='http://pypi.python.org/pypi/6px/',
	license='LICENSE',
	description='6px python sdk',
	long_description=open(os.path.abspath('./README.md')).read(),
)
