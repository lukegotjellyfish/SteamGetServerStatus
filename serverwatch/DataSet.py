import datetime
import pandas

dataset = []
csvFile = pandas.read_csv("ServerWatch.csv")
dates = csvFile["Date"]
times = csvFile["Time"]
players = csvFile["Players"]

for x, date in enumerate(dates, start=0):
	if date != "\x1a":
		dataset.append([date, times[x], players[x]])
	#print([date, times[x], players[x]])

dayPlayerCount = [
	[],
	[],
	[],
	[],
	[],
	[],
	[]
]

timePlayerCount = [
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
	[],
]

dayAnalysis = {}

for item in dataset:
	if item[0].count("/") > 0:
		_dmy = item[0].split("/")
	else:
		_dmy = item[0].split("-")
	#print(item[1])
	_hms = item[1].split(":")
	#print(_dmy, _hms)

	_seconds = int(round(float(_hms[2]),0))
	if _seconds == 60:
		_seconds = 59

	if int(_dmy[0]) < 34:
		_date = datetime.datetime(int(_dmy[2]), int(_dmy[1]), int(_dmy[0]),
								  int(_hms[0]), int(_hms[1]), _seconds)
	else:
		_date = datetime.datetime(int(_dmy[0]), int(_dmy[1]), int(_dmy[2]),
								  int(_hms[0]), int(_hms[1]), _seconds)


	dayPlayerCount[_date.weekday()].append(item[2])
	timePlayerCount[_date.hour].append(item[2])

	_dateDayMonth = [_date.day, _date.month, _date.year]
	#print(_dateDayMonth)


print("\nTimezone UTC+0\n")

_index = 0
_days = ["   Monday","  Tuesday","Wednesday"," Thursday","   Friday"," Saturday","   Sunday"]
for item in dayPlayerCount:
	_weekDay = _days[_index]
	print("Average players on a " + _weekDay + ": " + '{:.13f}'.format(sum(item)/len(item)) + " | Datapoints: " + str(len(item)))
	_index += 1

print("")

_index = 0
for item in timePlayerCount:
	indexStr = str(_index)
	if _index < 10:
		indexStr = " " + indexStr
	#print(str(item))
	print("Average players at " + indexStr + ": " + '{:.13f}'.format(sum(item)/len(item)) + " | Datapoints: " + str(len(item)))
	_index += 1

