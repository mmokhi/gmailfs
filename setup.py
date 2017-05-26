from distutils.core import setup
import os

# Please run
# python setup.py install   

setup(
	name = 'gmailfs',
	author = 'Mahdi Mokhtari',
	author_email = 'mmokhi@FreeBSD.org',
	url = 'https://github.com/mmokhi/gmailfs',
	packages = ['gmailfs'],
	package_dir = {'gmailfs':'src/gmailfs/'},
	scripts = ['src/gmailfs/gmailfs.py'],
	datafiles = [('/usr/local/etc/gmailfs/gmailfs.conf', ['src/gmailfs/conf/gmailfs.conf'])],
)
