import pandas
import datetime


class serverStats():
	days = ["   Monday","  Tuesday","Wednesday"," Thursday","   Friday"," Saturday","   Sunday"]

	def __init__(self,_address):
		self.address = _address
		self.dataset = []
		self.weekdayPlayerCountList =  [
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
		self.weekPlayerCount = [
			[[],[],[],[],[],[],[]],
			[[],[],[],[],[],[],[]],
			[[],[],[],[],[],[],[]],
			[[],[],[],[],[],[],[]],
			[[],[],[],[],[],[],[]],
			[[],[],[],[],[],[],[]],
			[[],[],[],[],[],[],[]],
			[[],[],[],[],[],[],[]],
			[[],[],[],[],[],[],[]],
			[[],[],[],[],[],[],[]],
			[[],[],[],[],[],[],[]],
			[[],[],[],[],[],[],[]],
			[[],[],[],[],[],[],[]],
			[[],[],[],[],[],[],[]],
			[[],[],[],[],[],[],[]],
			[[],[],[],[],[],[],[]],
			[[],[],[],[],[],[],[]],
			[[],[],[],[],[],[],[]],
			[[],[],[],[],[],[],[]],
			[[],[],[],[],[],[],[]],
			[[],[],[],[],[],[],[]],
			[[],[],[],[],[],[],[]],
			[[],[],[],[],[],[],[]],
			[[],[],[],[],[],[],[]],
			[[],[],[],[],[],[],[]],
			[[],[],[],[],[],[],[]],
			[[],[],[],[],[],[],[]],
			[[],[],[],[],[],[],[]],
			[[],[],[],[],[],[],[]],
			[[],[],[],[],[],[],[]],
			[[],[],[],[],[],[],[]],
			[[],[],[],[],[],[],[]],
			[[],[],[],[],[],[],[]],
			[[],[],[],[],[],[],[]],
			[[],[],[],[],[],[],[]],
			[[],[],[],[],[],[],[]],
			[[],[],[],[],[],[],[]],
			[[],[],[],[],[],[],[]],
			[[],[],[],[],[],[],[]],
			[[],[],[],[],[],[],[]],
			[[],[],[],[],[],[],[]],
			[[],[],[],[],[],[],[]],
			[[],[],[],[],[],[],[]],
			[[],[],[],[],[],[],[]],
			[[],[],[],[],[],[],[]],
			[[],[],[],[],[],[],[]],
			[[],[],[],[],[],[],[]],
			[[],[],[],[],[],[],[]],
			[[],[],[],[],[],[],[]],
			[[],[],[],[],[],[],[]],
			[[],[],[],[],[],[],[]],
			[[],[],[],[],[],[],[]],
			[[],[],[],[],[],[],[]],
			]
		
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

			self.weekdayPlayerCountList[_date.weekday()].append(item[2])
			self.timePlayerCount[_date.hour].append(item[2])
			if _date.isocalendar()[1] == 52:
				if _date.month == 1:
					self.weekPlayerCount[0][_date.weekday()].append(item[2])
				else: 
					self.weekPlayerCount[_date.isocalendar()[1]][_date.weekday()].append(item[2])
			else:
				self.weekPlayerCount[_date.isocalendar()[1]][_date.weekday()].append(item[2])

	def weekdayPlayerCount(self):
		lastAvgPlayers = 0
		for _index, item in enumerate(self.weekdayPlayerCountList,start=0):
			curAvgPlayers = sum(item)/len(item)
			dayString = "Average players on a " + self.days[_index] + ": " + '{:.13f}'.format(curAvgPlayers) + " | Datapoints: " + str(len(item))
			if lastAvgPlayers != 0:
				print(dayString + " | Diff: " + str(curAvgPlayers-lastAvgPlayers))
			else:
				print(dayString)
			lastAvgPlayers = curAvgPlayers
	
	def timePlayerCountReport(self):
		lastAvgPlayers = 0
		for _index,item in enumerate(self.timePlayerCount,start=0):
			indexStr = str(_index)
			if _index < 10:
				indexStr = " " + indexStr
		
			curAvgPlayers = sum(item)/len(item)
			hourString = "Average players at " + indexStr + ": " + '{:.13f}'.format(sum(item)/len(item)) + " | Datapoints: " + str(len(item))
			if lastAvgPlayers != 0:
				print(hourString + " | Diff: " + str(curAvgPlayers-lastAvgPlayers))
			else:
				print(hourString)
			lastAvgPlayers=curAvgPlayers
	
	def dayPlayerCount(self):
		lastAvgPlayers = 0
		
		weekNum = 0
		dayNum = 0
		for _index,item in enumerate(self.weekPlayerCount,start=0):
			indexStr = str(_index+1)
			if _index < 9:
				indexStr = " " + indexStr
	
			dayNum = weekNum
			if len(item) > 0:
				#item = [monday,tuesday,wednesday,thursday,friday,saturday,sunday]
				for __index, _item in enumerate(item,start=0):
					if len(_item) > 0:
						curAvgPlayers = sum(_item)/len(_item)
						dayString = "Average players on day " + str(dayNum) + ": " + '{:.13f}'.format(curAvgPlayers) + " | Datapoints: " + str(len(_item))
						print(dayString + " | Diff: " + str(curAvgPlayers-lastAvgPlayers))
						#print(f"dayNum = {dayNum}|_index = {_index}|__index = {__index}")
						lastAvgPlayers = curAvgPlayers
					dayNum += 1
			weekNum += 7

			curAvgPlayers = sum(item)/len(item)
			hourString = "Average players at " + indexStr + ": " + '{:.13f}'.format(sum(item)/len(item)) + " | Datapoints: " + str(len(item))
			if lastAvgPlayers != 0:
				print(hourString + " | Diff: " + str(curAvgPlayers-lastAvgPlayers))
			else:
				print(hourString)
			lastAvgPlayers=curAvgPlayers

	def weekPlayerCountReport(self):
		lastAvgPlayers = 0
		for _index,item in enumerate(self.weekPlayerCount,start=0):
			#Overwrite for a lazyfix to new weekPlayerCount structure
			newItem = []
			for day in item:
				for dayValue in day:
					newItem.append(dayValue)
			item = newItem
	
			indexStr = str(_index+1)
			if _index < 9:
				indexStr = " " + indexStr
	
			datapoints = len(item)
			if datapoints > 0:
				curAvgPlayers = sum(item)/len(item)
				weekString = "Average players on week " + indexStr + ": " + '{:.13f}'.format(curAvgPlayers).zfill(2) + " | Datapoints: " + str(datapoints)
				if lastAvgPlayers != 0:
					print(weekString + " | Diff: " + str(curAvgPlayers-lastAvgPlayers))
				else:
					print(weekString)
				lastAvgPlayers=curAvgPlayers
			

usFive = serverStats("51.79.37.206:2303")
euThree = serverStats("135.125.140.176:2303")

csvFile = pandas.read_csv("ServerWatch_2022.csv")
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


print("US5 Server Stats")
print("Timezone UTC+0")
print("From " + str(usFive.dataset[0][0]) + " " + str(usFive.dataset[0][1]) + " to " + str(usFive.dataset[-1][0]) + " " + str(usFive.dataset[-1][1]) + "\n")
usFive.weekdayPlayerCount()
print("")
usFive.timePlayerCountReport()
print("")
usFive.weekPlayerCountReport()
print("")
#usFive.dayPlayerCount()


print("\n\n\n")


print("EU3 Server Stats")
print("Timezone UTC+0")
print("From " + str(euThree.dataset[0][0]) + " " + str(euThree.dataset[0][1]) + " to " + str(euThree.dataset[-1][0]) + " " + str(euThree.dataset[-1][1]) + "\n")
euThree.weekdayPlayerCount()
print("")
euThree.timePlayerCountReport()
print("")
euThree.weekPlayerCountReport()
print()
euThree.dayPlayerCount()
input("PAUSE")
