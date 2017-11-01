import sys
import traceback

from lib import sources

errors = []

def add_exception(e):
	exc_type, exc_value, exc_traceback = sys.exc_info()

	errors.append({
		'message':get_message(e),
		'traces':traceback.format_exception(exc_type, exc_value, exc_traceback)
	})

def get_message(e):
	error_type = type(e)

	if error_type is sources.SourceErrorNoConfig:
		return 'Source configuration file is missing.'

	if error_type is sources.SourceErrorUnreadable:
		return 'Source configuration file is not readable.'

	if error_type is sources.SourceErrorNotJson:
		return 'Source configuration file is not valid JSON.'

	return '{}: "{}"'.format(e.__class__.__name__, str(e))

def output_all():
	if not len(errors):
		return

	print('-'*80)
	print('The following errors were encountered:\n')
	for error in errors:
		print(error['message'])
		[print(trace) for trace in error['traces']]
