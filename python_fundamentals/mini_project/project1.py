import sys

miles_to_travel = int(input("How far would you like to travel in miles ?"))

vechile = "Bicycle"

if((miles_to_travel >3) and (miles_to_travel <=300)):
    vechile = "Motor-Cycle"
elif(miles_to_travel > 300):
    vechile ="Super-car"

Suggestion = "I Suggest " + vechile + " to your Desintation"

print(Suggestion)