import datetime
import pandas

class serverStats():
	days = ["   Monday","  Tuesday","Wednesday"," Thursday","   Friday"," Saturday","   Sunday"]

	def __init__(self,_address):
		self.address = _address
		self.dataset = []
		self.dayPlayerCount =  [
			[],
			[],
			[],
			[],
			[],
			[],
			[],]
		self.timePlayerCount = 	[
			[],
			[],
			[],
			[],
			[],
			[],
			[],
			[],
			[],
			[],
			[],
			[],
			[],
			[],
			[],
			[],
			[],
			[],
			[],
			[],
			[],
			[],
			[],
			[],]
		
	def addToDataset(self,value):
		self.dataset.append(value)
	
	def addToPlayerCount(self):
		for item in self.dataset:
			if item[0].count("/") > 0:
				_dmy = item[0].split("/")
			else:
				_dmy = item[0].split("-")

			_hms = item[1].split(":")
			_seconds = int(round(float(_hms[2]),0))

			if _seconds == 60:
				_seconds = 59

			if int(_dmy[0]) < 34:
				_date = datetime.datetime(int(_dmy[2]), int(_dmy[1]), int(_dmy[0]),
										  int(_hms[0]), int(_hms[1]), _seconds)
			else:
				_date = datetime.datetime(int(_dmy[0]), int(_dmy[1]), int(_dmy[2]),
										  int(_hms[0]), int(_hms[1]), _seconds)


			self.dayPlayerCount[_date.weekday()].append(item[2])
			self.timePlayerCount[_date.hour].append(item[2])
	
	def dayPlayerCountReport(self):
		for _index, item in enumerate(self.dayPlayerCount,start=0):
			print("Average players on a " + self.days[_index] + ": " + '{:.13f}'.format(sum(item)/len(item)) + " | Datapoints: " + str(len(item)))
	
	def timePlayerCountReport(self):
		for _index,item in enumerate(self.timePlayerCount,start=0):
			indexStr = str(_index)
			if _index < 10:
				indexStr = " " + indexStr
			print("Average players at " + indexStr + ": " + '{:.13f}'.format(sum(item)/len(item)) + " | Datapoints: " + str(len(item)))
	

usFive = serverStats("51.79.37.206:2303")
euThree = serverStats("135.125.140.176:2303")

csvFile = pandas.read_csv("ServerWatch.csv")
dates = csvFile["Date"]
times = csvFile["Time"]
players = csvFile["Players"]
address = csvFile["Address"]

for x, date in enumerate(dates, start=0):
	if date != "\x1a":
		if address[x] == usFive.address:
			usFive.addToDataset([date, times[x], players[x], address[x]])
		else:
			euThree.addToDataset([date, times[x], players[x], address[x]])
	#print([date, times[x], players[x]])

usFive.addToPlayerCount()
euThree.addToPlayerCount()


print("\nTimezone UTC+1")
print("From " + str(usFive.dataset[0][0]) + " " + str(usFive.dataset[0][1]) + " to " + str(usFive.dataset[-1][0]) + " " + str(usFive.dataset[-1][1]) + "\n")
usFive.dayPlayerCountReport()
print("")
usFive.timePlayerCountReport()


# print("\nTimezone UTC+1")
# print("From " + str(euThree.dataset[0][0]) + " " + str(euThree.dataset[0][1]) + " to " + str(euThree.dataset[-1][0]) + " " + str(euThree.dataset[-1][1]) + "\n")
# euThree.dayPlayerCountReport()
# print("")
# euThree.timePlayerCountReport()