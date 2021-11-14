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

# FileSystem : Defines the filesysem object.
class FileSystem(object):

	# Filesystem constructor.
	def __init__(self):
		self.initialized = False
		self.CWMM_FOLDER = None

	# Initialize the filesystem.
	def init(self):

		# Set the path to the CWMM folder.
		self.CWMM_FOLDER = os.path.join(os.getenv('LOCALAPPDATA'), "CWMM")

		# Make the CWMM Folder if not exist.
		if not self.MakeFolder(self.CWMM_FOLDER):
			return False

		# Make the CWMM Downloads Folder if not exist.
		if not self.MakeFolder(os.path.join(self.CWMM_FOLDER, "downloads")):
			return False

		# Make the CWMM Mods Folder if not exist.
		if not self.MakeFolder(os.path.join(self.CWMM_FOLDER, "mods")):
			return False

		# Make config.json
		self.MakeFile(os.path.join(self.CWMM_FOLDER, "config.json"))

		# TODO: Validate JSON.

		# No errors occurred.
		self.initialized = True
		return True

	# Make a folder if it does not exist.
	def MakeFolder(self, folder: str):
		if not os.path.exists(folder):
			os.makedirs(folder)
			
			# Double check folder creation.
			if not os.path.exists(folder):
				print(f"ERROR: Failed to create folder: {folder}.")
				return False

		print(f"NOTE: Folder exists: {folder}.")
		return True

	# Make a file if it does not exist
	def MakeFile(self, file: str):
		if not os.path.isfile(file):
			open(file, 'a').close()

			# Double check file creation.
			if not os.path.isfile(file):
				print(f"ERROR: Failed to create file: {file}.")
				return False

		print(f"NOTE: File exists: {file}.")
		return True
