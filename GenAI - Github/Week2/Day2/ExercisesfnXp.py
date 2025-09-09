#Exercise 1: What Are You Learning?
#Goal: Create a function that displays a message about what you’re learning.

def display_message():
     return("I am learning about functions in Python.")

#function call
learn = display_message()
print(learn)
#---------------------------------------------------------
#Exercise 2: What's your Favorite Book?
#Goal: Create a function that displays a message about a favorite book.

def favorite_book(title):
     return(f"One of my favorite books is {title}")
book = favorite_book("Gadsby")
print(book)
#----------------------------------------------------------------------------
#Exercise 3: Some Geography
#Goal: Create a function that describes a city and its country.

def describe_city(city,country="Unknown"):
     return(f"{city} is in {country}.")
city_description=describe_city("Paris" ,"France")
print(city_description)
city_description=describe_city("London","England")
print(city_description)
city_description=describe_city("Tokyo")
print(city_description)
#------------------------------------------------------------
#Exercise 4: Random
#Goal: Create a function that generates random numbers and compares them.

import random
def compare_number(user_number):
     random_num=random.randint(1,100)

     if user_number == random_num:
          print("Success!")
     else:
          print("Fail!")
          print(f"Your number: {user_number}")
          print(f"Random number: {random_num}")

compare_number(44)
compare_number(10)
#----------------------------------------------------------------------
#Exercise 5: Let's Create Some Personalized Shirts!
#Goal: Create a function to describe a shirt's size and message, with default values.

def make_shirt(size,text):
     return(f"The size of the shirt is {size} and the text is {text}")
shirt=make_shirt("S","hello world!")
print(shirt)
print("---------------------------------------------------")
#Modify the Function with Default Values
def make_shirt(size="L",text="I love Python"):
     return(f"The size of the shirt is {size} and the text is {text}.")
shirt=make_shirt()  #Default
print(shirt)
shirt=make_shirt(size="M")        #size m , txt=Default
print(shirt)
shirt=make_shirt(size="XL",text="LOVE")   #size s, txt=LOVE
print(shirt)
#----------------------------------------------------------------------
#Exercise 6: Magicians
#Goal: Modify a list of magician names and display them in different ways.

magician_names=['Harry Houdini', 'David Blaine', 'Criss Angel']
def show_magicians(magician_names):
    for name in magician_names:
        print(name)
show_magicians(magician_names)

# Create a Function to Modify the List
def make_great(magician_names):
     for name in magician_names:
          print(f"{name} the Great.")
make_great(magician_names)
#--------------------------------------------------------------------------
#Exerccise 7: Temperature Advice
#Goal: Generate a random temperature and provide advice based on the temperature range.

def get_random_temp():
     random_temp=random.randint(-10,40)
     return random_temp
temperature=get_random_temp()
print(f"temperature testing 1: {temperature} degrees Celsius.")

#Floating-Point Temperatures (Bonus)
def random_temp():
     random_temperature=random.uniform(-10,40)
     return random_temperature
temperature=random_temp()
print(f"temperature testing 2: {temperature} degrees Celsius.")

def main():
     temp=get_random_temp()
     print(f"The temperature right now is {temp} degrees Celsius.")
     if temp < 0:
          print("Brrr, that's freezing! Wear some extra layers today")
     elif 0 <= temp <=16:
          print("Quite chilly! Don't forget your coat.")
     elif 17 <= temp <= 23:
          print("Nice weather.")
     elif 24 <= temp <= 32:
          print("A bit warm, stay hydrated.")
     elif 32 <= temp <= 40:
          print("It's really hot! Stay cool")
     else:
          print("Weather is fine today!")
main()

#Month-Based Seasons (Bonus)
import calendar
def get_random_temp(user_month) :
     month=calendar.month_name[user_month]
     if user_month in [12,1,2]:
          season = "Winter"
          temperature = random.randint(-10,10)
          print(f"{month}, {season}, temperature {temperature} degrees celsius")
     elif user_month in [3,4,5]:
          season = "Spring"
          temperature = random.randint(10,20)
          print(f"{month}, {season}, temperature {temperature} degrees celsius")
     elif user_month in [6,7,8]:
          season = "Summer"
          temperature = random.randint(20,40)
          print(f"{month}, {season}, temperature {temperature} degrees celsius")
     elif user_month in [9,10,11]:
          season = "Autumn"
          temperature = random.randint(10,20)
          print(f"{month}, {season}, temperature {temperature} degrees celsius")
     else:
          print("Invalid Input!")
          return None

while True:
     user_month=int(input("Enter a month number[1 - 12]: "))
     if 1 <= user_month <= 12:
          get_random_temp(user_month)
          break
     else:
          print("Invalid input. Please enter a number from 1 to 12.")
#get_random_temp(user_month)
     