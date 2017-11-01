class Link:

	def __init__(self, nextLink=None):
		self.nextLink = nextLink

	def is_blocked(self, entry):
		if self._is_blocked(entry):
			return True

		if (self.nextLink):
			return self.nextLink.filter(entry)
		
		return False

