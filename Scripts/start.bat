@ECHO OFF
CLS

CD /D E:\USBBACKUP\GitHub\SteamGetServerStatus\Scripts


goto ServerStatus

:ServerStatus
Powershell -executionpolicy remotesigned -File "QueryServer.ps1"
call "FilterResponse.py"
timeout /t 300
goto ServerStatus