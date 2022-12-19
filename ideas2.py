destinations_list = ["Las Vegas", "New York", "Miami", "San Diego", "Los Angeles"]
restaurants_list = ["Steakhouse", "Pizza", "Japenese", "Family Style", "Buffet"]
transportation_list = ["Plane", "Car", "Train", "Bus", "Motorcycle"]
entertainment_list = ["Walking the Vegas Strip", "Going to Sea World", "Going to basketball game", "Going on a bike ride through Central Park", "Going to the beach"]

print("")
print('Welcome to your dream day vacation! We here at Dream Trips USA are here to take care you!')
print('If you are not sure where you would like to go no worries! We will plan your dream day vacation for you.')
print("")

import random
destination = random.choice(destinations_list)
transportation = random.choice(transportation_list)
entertainment = random.choice(entertainment_list)
restauraunt = random.choice(restaurants_list)

# Destination meesage and function 

destination_message = f"We have chosen for you to vacation in {destination} for the day."
print(destination_message)
print("")

answer = input("Is this location ok with you? Enter y/n: ")

def destination_change(answer):
    while answer != "y":
        global destination
        destination = random.choice(destinations_list)
        answer = input(f"We are sorry that you did not like that destination. We have selected {destination} as another option. Does this location work for you? ")
    else: 
        print(f"You have chosen {destination} for the location of your day trip! Now let's move on and pick how you will get there.")

destination_change(answer)

