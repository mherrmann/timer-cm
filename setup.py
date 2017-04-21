"""Measure execution time with a context manager

See:
https://github.com/mherrmann/timer-cm
"""

from setuptools import setup

description = 'Measure execution time with a context manager.'
setup(
	name='timer-cm',

	version='1.0',

	description=description,
	long_description=
		description + '\n\nHome page: https://github.com/mherrmann/timer-cm',
	url='https://github.com/mherrmann/timer-cm',

	author='Michael Herrmann',
	author_email='[my first name]@[my last name].io',

	license='MIT',

	platforms=['MacOS', 'Windows', 'Debian'],

	classifiers=[
		'Development Status :: 5 - Production/Stable',
		'Intended Audience :: Developers',
	
		'License :: OSI Approved :: MIT License',
	
		'Operating System :: OS Independent',
	
		'Programming Language :: Python',
		'Programming Language :: Python :: 2',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.2',
		'Programming Language :: Python :: 3.3',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
	
		'Topic :: Software Development :: Libraries',
		'Topic :: Software Development :: Libraries :: Python Modules'
	],

	keywords='timer context manager',

	py_modules=['timer_cm']
)