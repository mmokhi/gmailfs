from distutils.core import setup
import os

# Please run
# python setup.py install   

setup(
	name = 'gmailfs',
	version = '0.8.6',
	author = 'Mahdi Mokhtari',
	url = 'https://github.com/mmokhi/gmailfs',
	packages = ['gmailfs'],
	package_dir = {'gmailfs':'src/gmailfs/'},
	scripts = ['src/gmailfs/mount_gmailfs'],
	data_files = [('/usr/local/etc/gmailfs/', ['src/gmailfs/conf/gmailfs.conf'])],
)
