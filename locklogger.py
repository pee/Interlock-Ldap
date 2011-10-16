#
#
import logging
from time import strftime

class LockLogger:
			
	def __init__(self, filename, stdout = False):

		self.filename = filename
		self.stdout = stdout

		logging.basicConfig(filename = self.filename, level = logging.DEBUG)
	
	def log(self, message):

		currtime = strftime("%Y-%m-%d %H:%M:%S")
		currtime += " " + message
		logging.debug(currtime)

		if self.stdout == True:
			print message

