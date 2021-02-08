goto ServerStatus

:ServerStatus
Powershell -executionpolicy remotesigned -File "QueryServer.ps1"
call "FilterResponse.py"
timeout /t 300
goto ServerStatus