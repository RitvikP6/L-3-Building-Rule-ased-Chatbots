import re, random 
from colorama import Fore, init

init(autoreset = True)

destinations = {
    "beaches" : ['Bali', 'Maldives', 'Phuket'],
    "mountains" : ['Sahara', 'Swiss Alps', 'Himalayas'],
    "cities" : ['NYC', 'Tokyo', 'Dubai']  
        }

jokes = {
    " Why don't programmers like nature? Too many bUgs!",
    " Why did the computer go to the doctor? Becasue it had a virus!",
    " Why do travellers always feel warm? Because of their hotspots!"

}

def recommend():
    print(Fore.CYAN + 'TravelBot: Beaches, mountains, or cities?')
    preference = input(Fore.YELLOW + "You: ")
    preference = normalize_input(preference)

    if preference in destinations:
        suggestion = random.choice(destinations[preference])
        print(Fore.GREEN + f"TravelBot: How about {suggestion}")
        print(Fore.CYAN + "TravelBot: Dou you like it? [Yes,No]")
        answer = input(Fore.YELLOW + "You: ").lower()

        if answer == 'yes':
            print(Fore.GREEN + f"TravelBot: Awesome! Enjoy {suggestion}!")
        elif answer == 'no':
            print(Fore.RED + "TravelBot: Lets try another.")
            recommend()
        else:
            print(Fore.RED + "TravelBot: I'll suggest again.")
            recommend()
    else:
        print(Fore.RED + "TravelBot: Sorry, I dont have that type of destination.")
    show_help()

def packing_tips():
    print(Fore.CYAN + "TravelBot: Where to?")
    location = normalize_input(input(Fore.YELLOW + 'You: '))
    print(Fore.CYAN + "TravelBot: How many days?")
    days = input(Fore.YELLOW + "You: ")

    print(Fore.GREEN + f"TravelBot: Packing tips for {days} days in {location}:")
    print(Fore.GREEN + " Pack Versatile Clothes")
    print(Fore.GREEN + " Bring chargers ? adapters")
    print(Fore.GREEN + "Check the weather forecast")

def tell_joke():
    print(Fore.YELLOW + F"TravelBot: {random.choice(jokes)}")

def show_help():
    print(Fore.MAGENTA + "\nI can")
    print(Fore.GREEN + "Suggest travel spots (say 'recommendation)")
    print(Fore.GREEN + "Offer Packing Tips (say 'packing')")
    print()