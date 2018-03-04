class Poller(object):
	FILENAME = "poll.txt"

	def WriteAt(self, at, value):
		with open(self.FILENAME,"r+") as file:
			line = file.read()
			print("Before: ", line)
			stringList = list(line)
			stringList[at] = value
			line = str(''.join(stringList))
			print("After: ", line)
			deleteContent(file)
			file.write(line)

def deleteContent(pfile):
	pfile.seek(0)
	pfile.truncate()

poller = Poller()
poller.WriteAt(0, "0")
