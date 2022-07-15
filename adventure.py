import time
import data
import random


def intro():
    print_pause("Are you ready for a road trip?")
    print_pause("All the bags are already packed") 
    print_pause("in the car is ready and fueled.")



myState = ["New York", "Alabama", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Idaho", "IllinoisIndiana"]


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def autoeSelection(items): 
    print_pause("Your destination will be auto selected.")
    milex = str(random.randint(300, 1000))
    name = input(" What is your name ? \n")
    # print(random.choice(myState))
    selected1 = random.choice(myState)
    if name != "":
        print_pause(f"{name}  your destination will be {selected1}")
    elif name == "":
        print_pause("Invalid name")
        print_pause(f"{name}  but your destination will be {selected1}")
    print_pause(f"your GPS Displays {milex} for your journey")
    mile = input("Are your ready to go  Yes or No? \n")
    if mile.lower() == "yes":
        print_pause(f"Destination is: {milex} miles")
    elif mile.lower() == "no":
        print_pause("Route pending...")
    else:
        print("Invalid, but input, Route pending... ")
    if "road" in items:
        print_pause(f"Maybe an overnight hotel \n"
                    "Before you reach your final destination, "
                    "but you think {selected1} worth it.")
        if milex in items:
            print_pause(milex + " still a long way to go")
            print_pause("and you think just 1 driver is" 
                        "not enough for the trip!")
        else:
            print_pause(f"You consider it's better to think twice" 
                        "because {milex}  it's a lot "
                        "You head back home thinking about changing" 
                        "your trip destination..")
            destination(items)
    else:
        print_pause("It looks like you need some helper or"
                    "another driver to cover those miles \n "
                    "You thinking of inviting a friend.")
        print_pause("You head back home .")
        destination(items)


def montana(items): 
    print_pause("You add your GPS destination for Sun Road Montana.")
    print_pause("After a few couple miles, there is"
                "a road closure on your way, "
                "The Cops stops to talk to you.")
    name = input(" What is your name ? \n")
    if name != "":
        print(name  + " take the next exit")
    elif name == "":
        print(" I understand you may have problem to"
                "talk but take the next exit")
    if "road closure" in items:
        print_pause("On the next exit, the earliest detour"
                    "is 30 minutes or 35 miles away "
                    "The car behind honking you but you still hesitat "
                    "then you decide it's not worth it.")
    else:
        print_pause("There is a gaz station close by  "
                    "just 4 miles away.")
        items.append("road closure")
    print_pause("You head back to home thinking to"
                "changing your trip destination.")
    destination(items)


def virginia(items):
    print_pause("You add the destination for Blue Ridge"
                "Parkway - Virginia on your GPS.")
    print_pause("After a few moments, you find the highway,"
                "and the road is clear low traffic "
                "the GPS shows destination is 8 hours"
                 "or 469 miles, and ask")
    mile = input("469 miles are your ready to proceed\n"
                 "Yes or No?")
    if mile.lower() == "yes":
        print("8 hours to your destination")
    elif mile.lower() == "no":
        print("Your destination is still pending...")
    else:
        print("Invalid iput\n"
        "Your destination is still pending...")
    if "road" in items:
        print_pause("Good way sunny road .")
        print_pause("You will take a break after 3 hours driving for fueling.")
    else:
        print_pause("Watch your speed. Some Parkways speed limit"
                    "is usually 45 MPH or less in certain places.")
        if "65" in items:
            print_pause("You know 65MPH hour will make"
                         "destination faster than 45 MPH "
                        "But you need to follows to road regulation.")
            items.append("road")
        else:
            print_pause("Ticket accident may happens. "
                        "65Mph  is the safest speed to make"
                        "your destination, and Blue Ridge Parkway"
                         "drive is a road trip you won't find anywhere else.")
    print_pause("But 8 hours or 469 miles, that's too much.\n"
                "You head back home thinking of changing"
                "your trip destination.")
    destination(items)


def washington(items):
    print_pause("You add your destination for Olympic"
                "Peninsula - Washington.")
    print_pause("your GPS Display 330 miles or 6 hours"
                "30 minutes for your journey "
                "Clear roads, no real traffic.")
    mile = input("330 miles are your ready to go  Yes or No? \n")
    if mile.lower() == "yes":
        print("6 hours 30 minutes to your destination")
    elif mile.lower() == "no":
        print("Your destination is still pending...")
    else:
        print("Invalid input, Your destination is still pending... ")
    if "road" in items:
        print_pause("6 to 7 hours road trip would required couple breaks.")
        print_pause("Maybe an overnight hotel "
                    "Before you reach your final destination, "
                    "but you think stunning views of the glistening"
                    "White Mountain tops of the Olympic ranges worth it.")
        if "330" in items:
            print_pause("330 still a long way to go")
            print_pause("and you think just 1 driver"
                        "is not enough for the trip!")
        else:
            print_pause("You consider it's better to think"
                        "twice because 330 miles it's a lot"
                        "You head back home thinking about"
                        "changing your trip destination..")
            destination(items)
    else:
        print_pause("It looks like you need some helper or another driver "
                    "You thinking of inviting a friend.")
        print_pause("You head back home .")
        destination(items)


def destination(items):
    print_pause("Please pick this destination for your gps "
                "which place you like to visit:")
    place = input("1. Going-to-the-Sun Road - Montana \n"
                  "2. Blue Ridge Parkway - Virginia \n"
                  "3. Olympic Peninsula - Washington \n"
                  "4. Auto Select - Random state options \n")
    if place == '1':
        montana(items)
    elif place == '2':
        virginia(items)
    elif place == '3':
        washington(items)
    elif place == '4':
        autoeSelection(items)


def play_game():
    items = []
    intro()
    destination(items)


play_game()
