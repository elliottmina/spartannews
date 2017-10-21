#!/usr/bin/env python3
import os
import time
from pprint import pprint

from lib import sources
from lib.processors.factory import build_processor
from lib.processors.factory import build_source
from lib import errors
from lib import last_run

def main():
	start_time = time.time()
	[process(path) for path in sources.sources()]
	output_errors()
	last_run.set(start_time)
	
def process(path):
	try:
		start_message(path)

		config = sources.get_config(path)
		processor = build_processor(config)
		source = build_source(config)
		processor.process(source)

	except sources.SourceError as e:
		errors.add(e, path)
		print_submessage(errors.errors[-1]['message'])
		print_submessage('Skipping source.\n')

	except Exception as e:
		errors.add(e, path)
	

def print_submessage(message):
	print('> {}'.format(message))

def start_message(path):
	source_name = os.path.basename(path)
	print('Processing source "{}"'.format(source_name))

def output_errors():
	if len(errors.errors):
		print('-'*80)
		print('The following errors were encountered during generation:\n')
		for error in errors.errors:
			print('Source: {}\nMessage: {}'.format(error['source'], error['message']))
			for trace in error['trace']:
				print(trace)




main()
