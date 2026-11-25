import sys

list_of_peoples = {"Jeff": "Is afraid of Dogs", "David": "Plays the piano", "Jason": "Can fly an aeroplane"}

for key, value in list_of_peoples.items():
    print(key, ":", value)

cp_list_of_peoples = list_of_peoples.copy()

list_of_peoples["Jeff"] = "Is afraid of heights"

for key, value in list_of_peoples.items():
    print(key, ":", value)

list_of_peoples["Jill"] = "Can hula dance"

for key, value in list_of_peoples.items():
    print(key, ":", value)