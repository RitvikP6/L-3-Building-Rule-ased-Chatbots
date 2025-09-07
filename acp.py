import re
import random
import datetime
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

# Sample jokes list
jokes = [
    "😂 Why don't programmers like nature? Too many bugs!",
    "🤣 Why did the computer go to the doctor? Because it caught a virus!",
    "😎 Why do travelers feel warm? Because of their hot spots!"
]

# Sample weather data (for demo, replace with live API if needed)
weather_data = {
    "delhi": "☀️ Sunny, 35°C",
    "mumbai": "🌧️ Rainy, 28°C",
    "hyderabad": "⛅ Cloudy, 30°C",
    "bangalore": "🌦️ Light showers, 26°C",
    "chennai": "🌤️ Humid, 33°C"
}

# Sample news headlines
news_headlines = [
    "📰 Breaking: Stock markets hit an all-time high!",
    "🌎 Scientists discover new exoplanet similar to Earth!",
    "💻 AI is revolutionizing the way we work and live.",
    "🏏 India wins the T20 World Cup 2025!",
    "🚀 SpaceX successfully launches its next-gen spacecraft."
]

# Helper function to normalize input
def normalize_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())

# Function to get weather info
def get_weather():
    print(Fore.CYAN + "WeatherBot: Please enter your city name:")
    city = normalize_input(input(Fore.YELLOW + "You: "))

    if city in weather_data:
        print(Fore.GREEN + f"WeatherBot: The current weather in {city.title()} is {weather_data[city]}")
    else:
        print(Fore.RED + "WeatherBot: Sorry, I don't have weather info for that city.")

# Function to get news headlines
def get_news():
    print(Fore.CYAN + "NewsBot: Here are today's top headlines:")
    for i, headline in enumerate(news_headlines, start=1):
        print(Fore.GREEN + f"{i}. {headline}")

# Function to get local time
def get_local_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p, %A, %d %B %Y")
    print(Fore.CYAN + f"TimeBot: The current local time is: {Fore.GREEN}{current_time}")

# Function to tell a random joke
def tell_joke():
    print(Fore.YELLOW + f"JokeBot: {random.choice(jokes)}")

# Help menu
def show_help():
    print(Fore.MAGENTA + "\nI can help you with:")
    print(Fore.GREEN + "- Get weather info (type 'weather')")
    print(Fore.GREEN + "- Show latest news (type 'news')")
    print(Fore.GREEN + "- Tell the local time (type 'time')")
    print(Fore.GREEN + "- Make you laugh with a joke (type 'joke')")
    print(Fore.GREEN + "- Type 'exit' or 'bye' to quit.\n")

# Main chatbot loop
def chat():
    print(Fore.CYAN + "🤖 Hello! I'm InfoBot – Your Weather, News, and Time Assistant.")
    name = input(Fore.YELLOW + "What's your name? ")
    print(Fore.GREEN + f"Hi {name}! Let's get started 🙂")

    show_help()

    while True:
        user_input = normalize_input(input(Fore.YELLOW + f"{name}: "))

        if "weather" in user_input:
            get_weather()
        elif "news" in user_input:
            get_news()
        elif "time" in user_input or "local time" in user_input:
            get_local_time()
        elif "joke" in user_input or "funny" in user_input:
            tell_joke()
        elif "help" in user_input:
            show_help()
        elif "exit" in user_input or "bye" in user_input:
            print(Fore.CYAN + "InfoBot: Goodbye! Stay informed 🌟")
            break
        else:
            print(Fore.RED + "InfoBot: Sorry, I didn't understand. Type 'help' to see commands.")

# Run the chatbot
if __name__ == "__main__":
    chat()
