import sock352
import struct

sock352.init('8000','3221')
mysocket = sock352.socket()
givenHeader = mysocket.connect(("localhost",1111))
x = struct.unpack("!12B", givenHeader)
print (x)