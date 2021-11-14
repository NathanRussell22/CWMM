# CWMM - Call Of Duty World At War Map Manager

# Import required libraries.
try:
	import os
	import sys
	import json
	import requests
except ImportError as importError:
	print("ERROR: ImportError occurred:\n{importError}")
	exit(-1)

# Mods : Defines the mods object.
class Mods(object):

	# Mods contructor.
	def __init__(self):
		self.name = None
		self.webpage = None
		self.developers = []
		self.download_urls = []
		self.description = None
		self.video = None
		self.image = None
		self.icon = None
		self.installed = False
		self.initialized = False

	# Initialize the mod object.
	def init(self, name: str, webpage: str, developers: [], download_urls: [], description: str, image=None, video=None, icon=None):

		# Make sure lists only contain strings.

		# Developers.
		for x in developers:
			if isintance(x, str):
				self.developers.append(x)

		# Downloads.
		for x in download_urls:
			if isintance(x, str):
				self.download_urls.append(x)

		# Update local variables.
		self.name = name
		self.webpage = webpage
		self.description = description
		self.image = image
		self.video = video
		self.icon = icon
		self.initialized = True

	# Download.
	def download(self):

		# Make sure the mod is initialized.
		if not self.initialized:
			print(f"ERROR: Can't download non-initialized mod: {self.name}.")
			return False


