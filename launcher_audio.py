import playsound3
from mutagen.wave import WAVE
import math

class AudioPlayerClass:
	def __init__(self, path):
		self.path = path
		self.length = 1000

		self.get_length()

	def get_length(self):
		wav = WAVE(self.path)
		self.length = math.ceil(wav.info.length*1000)

	def play_audio(self):
		playsound3.playsound(self.path, block=False)