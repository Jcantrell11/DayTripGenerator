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

# Transportation message and function 
transportation_message = f"We have now chosen for you to travel to your destination by {transportation}."
print(transportation_message)

answer = input("Does this travel method work for you? Enter y/n: ")

def transportation_change(answer):
    while answer != "y":
        global transportation
        transportation = random.choice(transportation_list)
        answer = input(f"We are sorry that you did not like that mode of transportaion. How about traveling by {transportation}. Does this transportation method work for you? ")
    else:
        print(f"You have chosen to travel by {transportation}. Great choice! Now let's move on to entertainment options.")

transportation_change(answer)

# Entertainment message and function
entertainment_message = f"We have now chosen for your entertainment to {entertainment}."
print(entertainment_message)

answer = input("Does this entertainment option work for you? Enter y/n: ")

def entertainment_change(answer):
    while answer != "y":
        global entertainment
        entertainment = random.choice(entertainment_list)
        answer = input(f"We are sorry that you did not like that mode of transportaion. How about traveling by {entertainment}. Does this transportation method work for you? ")
    else:
        print(f"You have chosen to {entertainment}. We think you will really enjoy doing that activity. Let's finally pick what you will have for dinner.")

entertainment_change(answer)

# Restaraunt message and fucntion
restauraunt_message = f"We have now chosen for you to eat at a {restauraunt} restauraunt for dinner."
print(restauraunt_message)

answer = input("Does this dinner option work for you? Enter y/n: ")

def restauraunt_change(answer):
    while answer != "y":
        global restauraunt
        restauraunt = random.choice(restaurants_list)
        answer = input(f"We are sorry that you did not this dinner option. How about eating at a {restauraunt} restauraunt. Does this food option work for you? ")
    else:
        print(f"You have chosen to eat at a {restauraunt} restaurant.")

restauraunt_change(answer)

confirm_message = input(f"Congratulations your dream day trip is planned. You have chosen to go to {destination} traveling via {transportation}. You will be {entertainment} and eating dinner at a {restauraunt} restauraunt. Please confirm that all of this is correct. Enter y if confirmed.")
print(confirm_message)

# options_transportation = random.choice(destinations_list)
# # for input in answer:
# if answer == "y":
#     print("Awesome Choice! You will really enjoy it there. Now let's move on to your transportation.")
# elif answer == 'n':
#     print(f"Well I am sorry to hear that you don't like that location! How about {options_transportation}?")
         
         


     
# agent_choice = (random.choice(destinations_list))
# print("We have chosen"); print(agent_choice); print("for your destination. Will this destination work for you?")


