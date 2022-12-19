destinations_list = ["Las Vegas", "New York", "Miami", "San Diego", "Los Angeles"]
restaurants_list = ["Steakhouse", "Pizza Joint", "Japenese Restaurant", "Family Style", "Buffet Restaurant"]
transportation_list = ["Plane", "Car", "Train", "Bus", "Motorcycle"]
entertainment_list = ["Walking the Vegas Strip", "Going to Sea World", "Going to basketball game", "Going on a bike ride through Central Park", "Going to the beach"]

print("")
print('Welcome to your dream day vacation! We here at Dream Trips USA are here to take care you!')
print('If you are not sure where you would like to go no worries! We will plan your dream day vacation for you.')
print("")

import random

def destination_message():
    destination = "We have chosen for you to vacation in" + " " + random.choice(destinations_list) + " " + "for the day!"
    print(destination)

destination_message()
print("")

answer = input("Is this location ok with you? Enter y/n: ")
options_transportation = random.choice(destinations_list)
for input in answer:
    if answer == "y":
        print("Awesome Choice! You will really enjoy it there. Now let's move on to your transportation.")
    elif answer == 'n':
        print(f"Well I am sorry to hear that you don't like that location! How about {options_transportation}? {answer}")
       
         


     
# agent_choice = (random.choice(destinations_list))
# print("We have chosen"); print(agent_choice); print("for your destination. Will this destination work for you?")


