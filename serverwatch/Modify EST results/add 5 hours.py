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
								int(_hms[0]), int(_hms[1]), _seconds) + datetime.timedelta(hours=5)
	else:
		_date = datetime.datetime(int(_dmy[0]), int(_dmy[1]), int(_dmy[2]),
								int(_hms[0]), int(_hms[1]), _seconds) + datetime.timedelta(hours=5)


	print(str(_date.day)    + "-" +
		  str(_date.month)  + "-" +
		  str(_date.year)   + "," +
		  str(_date.hour)   + ":" +
		  str(_date.minute) + ":" +
		  str(_date.second))
