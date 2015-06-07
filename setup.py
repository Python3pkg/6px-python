from distutils.core import setup

setup(
	name='px',
	version='0.0.1',
	author='cloud6',
	author_email='ops@cloud6.io',
	packages=['_cloud6'],
    url='https://github.com/cloud6-io/cloud6-python',
	license='MIT',
	description='Python module for cloud6',
	install_requires=['websocket-client']
)
