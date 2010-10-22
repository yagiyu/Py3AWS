from distutils.core import setup
from sys import version
if version < '2.2.3':
	from distutils.dist import DistributionMetadata
	DistributionMetadata.classifiers = None
	DistributionMetadata.download_url = None


setup(name='py3aws',
	version='0.0.1',
	package_dir={'py3aws': ''},
	packages=['py3aws'],
	author='Yu Yagi',
	author_email='yagi@yagi.sh', 
	description='A Python3 wrapper for Amazon Web Service',
	long_description='PyAWS3 is a Python3 wrapper for the latest Amazon Web Service. It is forked from PyAWS.', 
	url='http://www.yagi.sh/',
	license='Python Software Foundation License',
	platforms='OS Independent',
	download_url='http://prdownloads.sourceforge.net/pyaws/pyaws-0.1.0.tar.gz?download',
	classifiers=[
		'Development Status :: 2 - Pre-Alpha',
		'Environment :: Web Environment',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: Python Software Foundation License',
		'Operating System :: OS Independent',
		'Programming Language :: Python',
		'Topic :: WWW/HTTP',
    ]
)
