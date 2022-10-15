import pandas
import datetime
from colorama import init, Fore, Style
init()


class serverStats():
	days = ["   Monday","  Tuesday","Wednesday"," Thursday","   Friday"," Saturday","   Sunday"]
	dayPlayerCountReportLength = 14
	dayPlayerCountReportColour = Fore.LIGHTRED_EX 
	weekPlayerCountReportColour = Fore.LIGHTRED_EX
	timePlayerCountReportColour = Fore.LIGHTRED_EX
	weekdayPlayerCountReportColour = Fore.LIGHTRED_EX
	datapointsColour = Fore.BLUE
	diffColour = Fore.MAGENTA

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

	def weekdayPlayerCountReport(self):
		lastAvgPlayers = 0
		for _index, item in enumerate(self.weekdayPlayerCountList,start=0):
			curAvgPlayers = sum(item)/len(item)
			dayString = f"{self.weekdayPlayerCountReportColour}Average players on a {self.days[_index]}: {(sum(item)/len(item)):05.2f} {self.datapointsColour}| Datapoints: {len(item):,}{Fore.WHITE}"
			if lastAvgPlayers != 0:
				print(f"{dayString} {self.diffColour}| Diff: {str(curAvgPlayers-lastAvgPlayers)}{Fore.WHITE}")
			else:
				print(dayString)
			lastAvgPlayers = curAvgPlayers
	
	def timePlayerCountReport(self):
		lastAvgPlayers = 0
		for _index,item in enumerate(self.timePlayerCount,start=0):
			curAvgPlayers = sum(item)/len(item)
			hourString = f"{self.timePlayerCountReportColour}Average players at {_index:02}: {curAvgPlayers:05.2f} {self.datapointsColour}| Datapoints: {len(item):,}{Fore.WHITE}"
			if lastAvgPlayers != 0:
				print(f"{hourString} {self.diffColour}| Diff: {curAvgPlayers-lastAvgPlayers}{Fore.WHITE}")
			else:
				print(hourString)
			lastAvgPlayers = curAvgPlayers

	def weekPlayerCountReport(self):
		lastAvgPlayers = 0
		for _index,item in enumerate(self.weekPlayerCount,start=0):
			#Overwrite for a lazyfix to new weekPlayerCount structure
			newItem = []
			for day in item:
				for dayValue in day:
					newItem.append(dayValue)
			item = newItem
	
			datapoints = len(item)
			if datapoints > 0:
				curAvgPlayers = sum(item)/len(item)
				weekString = f"{self.weekPlayerCountReportColour}Average players on week {_index+1:02}: {curAvgPlayers:05.2f} {self.datapointsColour}| Datapoints: {datapoints:,}{Fore.WHITE}"
				if lastAvgPlayers != 0:
					print(f"{weekString} {self.diffColour}| Diff: {curAvgPlayers-lastAvgPlayers}{Fore.WHITE}")
				else:
					print(weekString)
				lastAvgPlayers=curAvgPlayers

	def dayPlayerCountReport(self):
		lastAvgPlayers = 0
		weekNum = 0
		dayNum = 0
		dayReport = []

		for _index, week in enumerate(self.weekPlayerCount,start=0):
			indexStr = str(_index+1)
			if _index < 9:
				indexStr = " " + indexStr
	
			dayNum = weekNum
			if len(week) > 0:
				#week = [monday,tuesday,wednesday,thursday,friday,saturday,sunday]
				for __index, _item in enumerate(week,start=0):
					if len(_item) > 0:
						curAvgPlayers = sum(_item)/len(_item)
						dayString = f"{self.dayPlayerCountReportColour}Average players on day {dayNum:03}: {curAvgPlayers:05.2f} {self.datapointsColour}| Datapoints: {len(_item)}"
						dayReport.append(f"{dayString} {self.diffColour}| Diff: {curAvgPlayers-lastAvgPlayers}{Fore.WHITE}")
						# print(dayString + " | Diff: " + str(curAvgPlayers-lastAvgPlayers))
						# print(f"dayNum = {dayNum}|_index = {_index}|__index = {__index}")
						lastAvgPlayers = curAvgPlayers
					dayNum += 1
			weekNum += 7

		# Output day report
		if self.dayPlayerCountReportLength != 0:
			print(f"Average players per day for the last {self.dayPlayerCountReportLength} days")
		for day in dayReport[-self.dayPlayerCountReportLength:]:
			print(day)


usFive = serverStats("51.79.37.206:2303")
usFive.dayPlayerCountReportLength = 14  # default = 14
euThree = serverStats("135.125.140.176:2303")
euThree.dayPlayerCountReportLength = 14  # default = 14


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
	# print([date, times[x], players[x]])

usFive.addToPlayerCount()
euThree.addToPlayerCount()


print("US5 Server Stats")
print("Timezone UTC+0")
print("From " + str(usFive.dataset[0][0]) + " " + str(usFive.dataset[0][1]) + " to " + str(usFive.dataset[-1][0]) + " " + str(usFive.dataset[-1][1]) + "\n")
usFive.weekdayPlayerCountReport()
print("")
usFive.timePlayerCountReport()
print("")
usFive.weekPlayerCountReport()
print("")
usFive.dayPlayerCountReport()

print("\n\n\n")
print("EU3 Server Stats")
print("Timezone UTC+0")
print("From " + str(euThree.dataset[0][0]) + " " + str(euThree.dataset[0][1]) + " to " + str(euThree.dataset[-1][0]) + " " + str(euThree.dataset[-1][1]) + "\n")
euThree.weekdayPlayerCountReport()
print("")
euThree.timePlayerCountReport()
print("")
euThree.weekPlayerCountReport()
print()
euThree.dayPlayerCountReport()
input("PAUSE")
