from graphsciics import *
import os
import time

class Animation:
	def __init__(self, delay):
		self.frames = []
		self.delay = delay
	def addframe(self, obj):
		self.frames.append(obj)
	def display(self):
		os.system("clear")
		for shape in self.frames:
			shape.display()
			time.sleep(self.delay)
			os.system("clear")
