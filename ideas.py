destinations_list = ["Las Vegas", "New York", "Miami", "San Diego", "Los Angeles"]
restaurants_list = ["Steakhouse", "Pizza Joint", "Japenese Restaurant", "Family Style", "Buffet Restaurant"]
transportation_list = ["Plane", "Car", "Train", "Bus", "Motorcycle"]
entertainment_list = ["Walking the Vegas Strip", "Going to Sea World", "Going to basketball game", "Going on a bike ride through Central Park", "Going to the beach"]

print("")
print('Welcome to your dream day vacation! We here at Dream Trips USA are here to take care you!')
print('If you are not sure where you would like to go no worries! We will plan your dream day vacation for you.')
print("Here is the trip that was put together for you:")
print("")
import random

destination = random.choice(destinations_list)

destination_message = f"The destination that was chosen for you is {destination}"
transportation = "You will be traveling in style in a" + " " + random.choice(transportation_list) + "."
entertainment = "For your entertainment you will be" + " " + random.choice(entertainment_list) + "."
restaurants = "Finally, for dinner you will be visiting" + " " + random.choice(restaurants_list) + "."

print(destination_message)
print("")
print(transportation)
print("")
print(entertainment)
print("")
print(restaurants) 
print("")

answer = input("Is this location ok with you? Enter y/n: ")

def destination_change(answer):
    while answer != "y":
        destination = random.choice(destinations_list)
        answer = input(f"We are sorry that you did not like that destination. We have selected {destination} as another option. Does this location work for you? ")
    else:
        print(f"You have chosen {(destination)} for the location of your day trip! Now let's move on and pick how you will get there.") 
       

destination_change(answer)

