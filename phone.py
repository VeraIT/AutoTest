import requests
import time
import logging

logger = logging.getLogger()
logger.setLevel(level=logging.DEBUG)
file_handler = logging.FileHandler('syslog.log')
formatter = logging.Formatter('%(asctime)s - %(levelname)s : %(message)s [%(funcName)s]')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


class phone():
	"""定义一个话机的类"""
	def __init__(self, ip, ext='', username='', password=''):
		self.ip = ip
		self.ext = ext
		self.username = username
		self.password = password

	def dial(self, dst_ext):
		dial_url = "http://"+self.username+":"+self.password+"@"+self.ip+"/AutoTest&keyboard="+dst_ext
		try:
			dial= requests.get(dial_url)
			dial.raise_for_status()
		except requests.exceptions.Timeout as e:
			logger.debug(e)
		except requests.exceptions.ConnectionError as e:
			logger.debug(e)
		except requests.exceptions.HTTPError as e:
			logger.debug(e)

	def answer(self):
		answer_url = "http://"+self.username+":"+self.password+"@"+self.ip+"/AutoTest&keyboard=OK"
		try:
			dial= requests.get(answer_url)
			dial.raise_for_status()
		except requests.exceptions.Timeout as e:
			logger.debug(e)
		except requests.exceptions.ConnectionError as e:
			logger.debug(e)
		except requests.exceptions.HTTPError as e:
			logger.debug(e)

	def end_call(self):
		end_call_url = "http://"+self.username+":"+self.password+"@"+self.ip+"/AutoTest&keyboard=F4"
		try:
			dial= requests.get(end_call_url)
			dial.raise_for_status()
		except requests.exceptions.Timeout as e:
			logger.debug(e)
		except requests.exceptions.ConnectionError as e:
			logger.debug(e)
		except requests.exceptions.HTTPError as e:
			logger.debug(e)

