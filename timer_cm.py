from timeit import default_timer
from decimal import Decimal

class Timer(object):
	def __init__(self, name, print_results=True):
		self.elapsed = Decimal()
		self._name = name
		self._print_results = print_results
		self._start_time = None
		self._children = {}
	def __enter__(self):
		self.start()
		return self
	def __exit__(self, *_):
		self.stop()
		if self._print_results:
			self.print_results()
	def child(self, name):
		try:
			return self._children[name]
		except KeyError:
			result = Timer(name, print_results=False)
			self._children[name] = result
			return result
	def start(self):
		self._start_time = self._get_time()
	def stop(self):
		self.elapsed += self._get_time() - self._start_time
	def print_results(self):
		print(self._format_results())
	def _format_results(self, indent='  '):
		result = '%s: %.3fs' % (self._name, self.elapsed)
		children = self._children.values()
		for child in sorted(children, key=lambda c: c.elapsed, reverse=True):
			child_lines = child._format_results(indent).split('\n')
			child_percent = child.elapsed / self.elapsed * 100
			child_lines[0] += ' (%d%%)' % child_percent
			for line in child_lines:
				result += '\n' + indent + line
		return result
	def _get_time(self):
		return Decimal(default_timer())