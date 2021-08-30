#!/bin/bash
for (( ; ; ))
do
	pwsh -executionpolicy remotesigned -File "Query_EU3.ps1"
	python3 "FilterResponse.py"
	pwsh -executionpolicy remotesigned -File "Query_US5.ps1"
	python3 "FilterResponse.py"
	sleep 300
done