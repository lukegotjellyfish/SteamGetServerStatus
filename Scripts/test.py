from datetime import datetime

dateTaken  = str(datetime.now()).split(" ")
day        = dateTaken[0]
time       = dateTaken[1]

print(time[0:-7])