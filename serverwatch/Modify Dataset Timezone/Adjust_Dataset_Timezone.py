import datetime
import pandas
import csv

dataset = []
csvFile = pandas.read_csv("ServerWatch.csv")
dates = csvFile["Date"]
times = csvFile["Time"]
players = csvFile["Players"]
maxPlayers = csvFile["Max Players"]
version = csvFile["Version"]

timezoneAdjustment = 0

while timezoneAdjustment == 0:
	try:
		timezoneAdjustment = int(input("Dataset timezone adjustment:\n> "))
	except ValueError:
		input("Enter a number\n")

for x, date in enumerate(dates, start=0):
	if date != "\x1a":
		dataset.append([date, times[x], players[x], maxPlayers[x], version[x]])
	#print([date, times[x], players[x]])



for x, item in enumerate(dataset):
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
								int(_hms[0]), int(_hms[1]), _seconds) + datetime.timedelta(hours=timezoneAdjustment)
	else:
		_date = datetime.datetime(int(_dmy[0]), int(_dmy[1]), int(_dmy[2]),
								int(_hms[0]), int(_hms[1]), _seconds) + datetime.timedelta(hours=timezoneAdjustment)

	dataset[x][0] = f"{_date.year}-{_date.month}-{_date.day}"
	dataset[x][1] = f"{_date.hour:02}:{_date.minute:02}:{_date.second:02}"

	# print(str(_date.day)    + "-" +
	#	  str(_date.month)  + "-" +
	#	  str(_date.year)   + "," +
	#	  str(_date.hour)   + ":" +
	#	  str(_date.minute) + ":" +
	#	  str(_date.second))


with open("ServerWatch.csv", "r+", encoding='utf-8') as serverCsv:
	csvWriter = csv.writer(serverCsv, delimiter=',', lineterminator='\n')
	csvWriter.writerow(["Date","Time","Address","Players","Max Players","Version"])
	csvWriter.writerows(dataset)