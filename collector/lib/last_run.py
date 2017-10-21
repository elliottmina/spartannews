import time
import os
from pprint import pprint

from lib import config

data_file = config.BASE_DIR + '/data/lastrun'

def get():
	if not os.path.isfile(data_file):
		return 0

	with open(data_file, 'r') as handle:
		contents = handle.read()

	try:
		return float(contents)
	except ValueError:
		return 0

def set(timestamp):
	with open(data_file, 'w') as handle:
		handle.write(str(timestamp))
