# CWMM - Call Of Duty World At War Map Manager

if __name__ != "__main__":
	print("ERROR: __name__ != __main__, something went wrong...")
	exit(-1)

# Import required libraries.
try:
	import os
	import sys
	import pygame
	import requests
	from engine import Engine
except ImportError as importError:
	print("ERROR: ImportError occurred:\n{importError}")
	exit(-1)

# Pre-Processor Definitions. [This should be done prior to any initialization]
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Create a new engine instance.
engine = Engine()

# Initialize the engine instance.
if not engine.init():
	print("ERROR: Failed to initialize the engine.")
	sys.exit(-1)

# Applicaion main loop.
engine.main()

# Test downloads.
url = "https://tqxq8g.dm.files.1drv.com/y4mZeVRsYToaopAYYY-7oDCF0ro2ygFr8AprT8kZ4Uxus37vYqmIrN8ClcS3A8bhFZNpwJUi3xKW5ZGUEl927mCUswl4yPHe1WPSJHnJ2VSiOsN-SOePtUiIle2Qxs99_bxllkBlF0Fq64Y6FOVd-GVvNVx92_BFy2XfINkXb9Ukx4tnMClPu9fIYwQVoQTzOwy9ai3mvV2RXiCz6USyz48NA/nazi_zombie_mix.exe"

req = requests.get(url)
print(req.headers)

input()

name = req.url[url.rfind('/')+1:]
print(name)

print("Starting Download!")
with open(os.path.join("C:\\Users\\Russell\\AppData\\Local\\CWMM\\downloads", name), 'wb') as f:
	for chunk in req.iter_content(chunk_size=8192):
		if chunk:
			print(f"Downloading Data Chunk: {chunk}.")
			f.write(chunk)

# Exit the application.
sys.exit(0)
