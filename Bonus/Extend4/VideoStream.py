class VideoStream:
	def __init__(self, filename):
		self.filename = filename
		try:
			self.file = open(filename, 'rb')
		except:
			raise IOError
		self.frameNum = 0
		
	def nextFrame(self):
		"""Get next frame."""
		data = self.file.read(5) # Get the framelength from the first 5 bits
		if data: 
			framelength = int(data)
							
			# Read the current frame
			data = self.file.read(framelength)
			self.frameNum += 1
		return data
	
	def frameNbr(self):
		"""Get frame number."""
		return self.frameNum
	
	def next20Frame(self):
		"""Get 20 next frame."""
		for i in range (1, 19):
			self.nextFrame()
		print("FORWARD", self.frameNum)
		return self.nextFrame()
	
	def back20Frame(self):
		"""Get 20 back frame."""
		self.close()
		length = self.frameNum - 20
		length = length if length > 0 else 0
		self.__init__(self.filename)
		for i in range(length):
			self.nextFrame()
		print("BACKWARD", self.frameNum)
		return self.nextFrame()
	
	def close(self):
		try:
			self.file.close()
		except:
			pass