import dateutil.parser
import time

from lib.processors.feed.filters.link import Link
from lib.util import last_run

class Threshold(Link):

	def _is_blocked(self, entry):
		date = dateutil.parser.parse(entry.published)
		published = time.mktime(date.timetuple())
		if published <= last_run.get():
			return True
