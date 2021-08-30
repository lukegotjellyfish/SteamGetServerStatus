@ECHO OFF
CLS


goto ServerStatus

:ServerStatus
Powershell -executionpolicy remotesigned -File "Query_EU3.ps1"
call "FilterResponse.py"
Powershell -executionpolicy remotesigned -File "Query_US5.ps1"
call "FilterResponse.py"
timeout /t 300
goto ServerStatus