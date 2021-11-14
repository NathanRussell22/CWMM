# CWMM - Call Of Duty World At War Map Manager

# Import required libraries.
try:
	import os
	import sys
	import pygame
except ImportError as importError:
	print("ERROR: ImportError occurred:\n{importError}")
	exit(-1)

# Window : Defines the window object.
class Window(object):

	# Window constructor.
	def __init__(self):
		self.window = None
		self.caption = None
		self.width = None
		self.height = None
		self.clock = None
		self.fps = None
		self.fullscreen = False
		self.resizeable = False
		self.initialized = False

	# Initialize the window instance.
	def init(self, width: int, height: int, caption: str, fps: int):

		# Check if pygame has been initialized.
		if not pygame.get_init():
			print("ERROR: Tried to create a window prior to pygame initialization.")
			return False

		# Update local variables.
		self.width = width
		self.height = height
		self.caption = caption
		self.clock = pygame.time.Clock()
		self.fps = fps

		# Create a new pygame window.
		self.window = pygame.display.set_mode((self.width, self.height), pygame.HWSURFACE | pygame.DOUBLEBUF)

		# Set window caption.
		pygame.display.set_caption(self.caption)

		# If no errors occurred.
		self.initialized = True
		return True

	# Update the display.
	def update(self):
		if self.initialized:
			pygame.display.flip()
			self.clock.tick(self.fps)

	# close the window.
	def close(self):
		pygame.display.quit()
		self.initialized = False
