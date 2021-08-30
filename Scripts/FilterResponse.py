import csv
import os.path
from datetime import datetime

csvName="ServerWatch.csv"

if not (os.path.isfile(csvName)):
	with open(csvName, "a", encoding='utf-8') as serverCsv:
		csvreader = csv.writer(serverCsv, delimiter=',', lineterminator='\n')
		csvreader.writerow(["Date","Time","Players","Max Players","Address"])

newFile=[]
with open("PS-Response\\response.json", "r", encoding="utf-8") as j:
	lines = j.readlines()
	#[1:]remove first character
	line = lines[3].replace("; ","\n").replace("                  ","")
	line = line[4:-4]
	line = line.split("\n")

	dateTaken  = str(datetime.now()).split(" ")
	day        = dateTaken[0]
	time       = dateTaken[1]
	address    =  line[0].replace("addr=","")
	gameport   =  line[1].replace("gameport=","")
	steamid    =  line[2].replace("steamid=","")
	name       =  line[3].replace("name=","")
	appid      =  line[4].replace("appid=","")
	gamedir    =  line[5].replace("gamedir=","")
	version    =  line[6].replace("version=","")
	product    =  line[7].replace("product=","")
	region     =  line[8].replace("region=","")
	players    =  line[9].replace("players=","")
	maxPlayers = line[10].replace("max_players=","")
	bots       = line[11].replace("bots=","")
	gameMap    = line[12].replace("map=","")
	secure     = line[13].replace("secure=","")
	dedicated  = line[14].replace("dedicated=","")
	os         = line[15].replace("os=","")
	gametype   = line[16].replace("gametype=","")

	print(line)
	print("Written: " + str([day, time[0:-7], players, maxPlayers, address]))
	with open(csvName, "a", encoding='utf-8') as serverCsv:
		csvreader = csv.writer(serverCsv, delimiter=',', lineterminator='\n')
		csvreader.writerow([day, time[0:-7], players, maxPlayers, address])