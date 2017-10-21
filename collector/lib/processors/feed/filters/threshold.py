from email.utils import parsedate_tz
import time

from lib.processors.feed.filters.link import Link
from lib import last_run

class Threshold(Link):

	def _is_blocked(self, entry):
		published = time.mktime(parsedate_tz(entry.published)[0:9])
		if published <= last_run.get():
			return True
