destinations_list = ["Las Vegas", "New York", "Miami", "San Diego", "Los Angeles"]
restaurants_list = ["Steakhouse", "Pizza Joint", "Japenese Restaurant", "Family Style", "Buffet Restaurant"]
transportation_list = ["Plane", "Car", "Train", "Bus", "Motorcycle"]
entertainment_list = ["Walking the Vegas Strip", "Going to Sea World", "Going to basketball game", "Going on a bike ride through Central Park", "Going to the beach"]

def welcome():
    message = "Welcome to your dream day vacation! We here at Dream Trips USA are here to take care you! If you are not sure where you would like to go no worries! We will plan your dream day vacation for you."
    print(message)
welcome()


import random 
def transportation(): 
    intro = f"We will first pick out the location of your trip. We have chosen {random.choice(destinations_list)} for you. {input("Does this location work for you? Enter y/n:")}"
    print(intro)
    
transportation()


# import random 

# def destination_message():
#     destination = "We have chosen for you to vacation in" + " " + random.choice(destinations_list) + " " + "for the day!"
#     print(destination)

# destination_message()
# print("")

# answer = input("Is this location ok with you? Enter y/n: ")
# if answer == "n":
#     print(f"I am sorry that you don't like that location. How does {random.choice(destinations_list)} sound?")
# if answer == "y":
#     print("Awesome Choice! You will really enjoy it there. Now let's move on to your transportation.")


