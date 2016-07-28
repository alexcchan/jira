#!/usr/bin/python

from distutils.core import setup

setup(
	# Basic package information.
	name = 'jira',
	version = '0.0.0',
	packages = ['jira'],
	include_package_data = True,
	install_requires = ['httplib2', 'simplejson'],
	url = 'https://github.com/alexcchan/jira/tree/master',
	keywords = 'jira api',
	description = 'JIRA API v2 Wrapper for Python',
	classifiers = [
		'Development Status :: 4 - Beta',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Topic :: Software Development :: Libraries :: Python Modules',
		'Topic :: Internet'
	],
)


