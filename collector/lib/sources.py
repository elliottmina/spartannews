import json
from glob import glob
import os

from pprint import pprint


from lib import config

def sources():
	return glob(config.BASE_DIR + '/sources/*')

def get_config(source_path):
	config_path = source_path + '/config.json'

	if not os.path.isfile(config_path):
		raise SourceErrorNoConfig(config_path)

	try:
		with open(config_path) as handle:
			return json.load(handle)
	
	except IOError:
		raise SourceErrorUnreadable(config_path)

	except json.JSONDecodeError:
		raise SourceErrorNotJson(config_path)

class SourceError(RuntimeError): pass
class SourceErrorNoConfig(SourceError): pass
class SourceErrorUnreadable(SourceError): pass
class SourceErrorNotJson(SourceError): pass