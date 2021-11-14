# CWMM - Call Of Duty World At War Map Manager

# Import required libraries.
try:
	import os
	import sys
	import pygame
	from window import Window
	from filesystem import FileSystem
except ImportError as importError:
	print("ERROR: ImportError occurred:\n{importError}")
	exit(-1)

# Engine : Defines the engine object.
class Engine(object):

	# Engine constructor.
	def __init__(self):
		self.initialized = False
		self.filesystem = FileSystem()
		self.window = Window()
		self.busy = False

	# Initialize the Engine Instance.
	def init(self):

		# Initialize libraries.
		pygame.init()

		# Check if pygame initialized.
		if not pygame.get_init():
			print("ERROR: Failed to initialize pygame.")
			return False

		# Initialize the filesystem.
		if not self.filesystem.init():
			print("ERROR: Failed to initialize the filesystem.")
			return False

		# Initialize the pygame window.
		if not self.window.init(round(pygame.display.Info().current_w * (2.5/3)), round(pygame.display.Info().current_h * (2.5/3)), "CWMM", 60):
			print("ERROR: Failed to create the pygame window.")
			return False

		# No errors occurred.
		self.initialized = True
		return True

	# Terminate the engine.
	def close(self):
		pygame.quit()
		self.window.close()
		self.initialized = False

	# Application main loop.
	def main(self):

		# Make sure the engine is initialized.
		if self.initialized == False:
			print("Failed to initialize the engine.")
			sys.exit(-1)

		while self.initialized:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					if not self.busy:
						self.close()

			self.window.update()
