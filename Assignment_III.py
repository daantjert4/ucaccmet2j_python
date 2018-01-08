# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 12:40:15 2018

@author: Daan
"""
import json
with open('precipitation.json') as precipfile:
    precipfile = json.load(precipfile)

#Part2: yearly rain Seattle ## I did this first, since I didn't get the monthly part yet
rainlist = []
for dictline in precipfile:   
    if dictline['station'] == 'GHCND:US1WAKG0038':
        rainlist.append(dictline['value'])   
yearrain = sum(rainlist)    
print(yearrain) #this outputs the total rain for Seattle in this year

#Part1: montly rain Seattle
total_monthly_rain = []
monthslist = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11','12']
for month in monthslist:
    monthly_rain = []
    for dictline in precipfile:
        if dictline['station'] == 'GHCND:US1WAKG0038':  
                if dictline['date'].split('-')[1] == month:
                    monthly_rain.append(dictline['value'])
    total_monthly_rain.append(sum(monthly_rain))   
print(total_monthly_rain) #this is the list of monthly rain values in Seattle
print(sum(total_monthly_rain)) #shows the total of rain again (like part1), proves both parts are correct
 
 