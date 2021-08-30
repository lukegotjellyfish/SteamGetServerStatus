#!/bin/bash
while true
do
	pwsh -executionpolicy remotesigned -File "Query_EU3.ps1"
	python3 FilterResponse.py
	pwsh -executionpolicy remotesigned -File "Query_US5.ps1"
	python3 FilterResponse.py
	
	gdrive update 1aJhDTFRpzDCkzThP5qX0fxThnQ5AUr7F ServerWatch.csv
	
	sleep 300
done