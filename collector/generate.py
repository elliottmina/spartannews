#!/usr/bin/env python3
import sys
import os
import time

from lib import sources
from lib.processors.factory import build_processor
from lib.processors.factory import build_source
from lib.util import errors
from lib.util import last_run
from lib.util.persistor import EntryUpserter
from lib.util import database_initializer
from lib.util import output

start_time = None

def main():
	start_up()
	
	with EntryUpserter() as upserter:
		[process_source(upserter, path) for path in get_paths()]

	finish()

def start_up():
	global start_time

	start_time = time.time()
	database_initializer.initialize()

def get_paths():
	if len(sys.argv) > 1:
		output.message('Processing explicit source.')
		return [sys.argv[1]]
	return sources.sources()

def process_source(upserter, source_path):
	try:
		start_message(source_path)

		config = sources.get_config(source_path)
		processor = build_processor(config)
		source = build_source(config)
		processor.process(upserter, source)

	except sources.SourceError as e:
		errors.add_exception(e)
		output.submessage(errors.errors[-1]['message'])
		output.submessage('Skipping source.\n')

	except Exception as e:
		errors.add_exception(e)


def finish():
	errors.output_all()
	last_run.set(start_time)
	
def start_message(path):
	source_name = os.path.basename(path)
	output.message('Processing source "{}"'.format(source_name))

if __name__ == '__main__':
	main()
