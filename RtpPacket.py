import sys
from time import time
HEADER_SIZE = 12

class RtpPacket:	
	header = bytearray(HEADER_SIZE)
	
	def __init__(self):
		pass
		
	def encode(self, version, padding, extension, cc, seqnum, marker, pt, ssrc, payload):
        
		"""Encode the RTP packet with header fields and payload."""
        
		timestamp = int(time())
		header = bytearray(HEADER_SIZE)
		#--------------
		# TO COMPLETE
		#--------------
        
		# Fill the  with RTP header fields
		header[0] = (header[0] | version<<6)&0xC0;    	# Version        # 2 bits
		header[0] = (header[0] | padding << 5); 	# Padding        # 1 bit
		header[0] = (header[0] | extension << 4);       # Extension      # 1 bit
		header[0] = (header[0] | (cc & 0x0F));          # CSRC count     # 4 bits
		header[1] = (header[1] | marker << 7);          # Marker         # 1 bit
		header[1] = (header[1] | (pt & 0x7f));          # Payload type   # 7 bits
		header[2] = (seqnum & 0xFF00) >> 8;             # Sequence number: 16 bits total, this is the first 8 bits
		header[3] = (seqnum & 0xFF);                    # The remaining 8 bits
		header[4] = (timestamp >> 24);                  # Timestamp: 32 bit total, first 8 bits
		header[5] = (timestamp >> 16) & 0xFF;           # 2nd 8 bits
		header[6] = (timestamp >> 8) & 0xFF;            # 3rd 8 bits
		header[7] = (timestamp & 0xFF);                 # Last 8 bits
		header[8] = (ssrc >> 24);                       # SSRC: also 32 bit, first 8 bits
		header[9] = (ssrc >> 16) & 0xFF;                # 2nd 8 bits 
		header[10] = (ssrc >> 8) & 0xFF;                # 3rd 8 bits
		header[11] = ssrc & 0xFF                        # Last 8 bits
		self.header = header
		#Get the payload from the argument
		self.payload = payload
		
	def decode(self, byteStream):
		"""Decode the RTP packet."""
		self.header = bytearray(byteStream[:HEADER_SIZE])
		self.payload = byteStream[HEADER_SIZE:]
	
	def version(self):
		"""Return RTP version."""
		return int(self.header[0] >> 6)
	
	def seqNum(self):
		"""Return sequence (frame) number."""
		seqNum = self.header[2] << 8 | self.header[3]
		return int(seqNum)
	
	def timestamp(self):
		"""Return timestamp."""
		timestamp = self.header[4] << 24 | self.header[5] << 16 | self.header[6] << 8 | self.header[7]
		return int(timestamp)
	
	def payloadType(self):
		"""Return payload type."""
		pt = self.header[1] & 127
		return int(pt)
	
	def getPayload(self):
		"""Return payload."""
		return self.payload
		
	def getPacket(self):
		"""Return RTP packet."""
		return self.header + self.payload
