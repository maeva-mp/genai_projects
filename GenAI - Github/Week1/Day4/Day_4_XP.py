#Exercise 1:Favorite Numbers
# #Instructions:
#Create a set called my_fav_numbers and populate it with your favorite numbers.

my_fav_numbers = {7, 4, 6}
print("my_fav_numbers", my_fav_numbers)
#Add two new numbers to the set.
my_fav_numbers.add(8)
my_fav_numbers.add(5)
#Remove the last number you added to the set.
my_fav_numbers.remove(5)
#Create another set called friend_fav_numbers and populate it with your friend’s favorite numbers.
friend_fav_numbers= {1, 2, 3}
#Concatenate my_fav_numbers and friend_fav_numbers to create a new set called our_fav_numbers.
print("our_fav_numbers:", my_fav_numbers.union(friend_fav_numbers))

#Exercise 2:Tuple
#Instructions:
#Given a tuple of integers, try to add more integers to the tuple.
my_tuple=(5,6,7)
new_tuple= my_tuple + (4,8)
print(new_tuple)

#Exercise 3:List Manipulation
#Instructions:
#You have a list: basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket=["Banana", "Apples", "Oranges", "Blueberries"]
#Remove "Banana" from the list.
basket.remove("Banana")
#Remove "Blueberries" from the list
basket.pop(-1)
#Add "Kiwi" to the end of the list
basket.append("Kiwi")
#Add "Apples" to the beginning of the list.
basket.insert(0,"Apples")
#Count how many times "Apples" appear in the list
basket.count("Apples")
#Empty the list.
basket.clear()
#Print the final state of the list
print(basket)

#Exercise 4:Floats
#Instructions:
#reate a list containing the following sequence of mixed floats and integers:1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5.
#Avoid hard-coding each number manually.
numbers=[]
num=1.5
while num <= 5.0:
    numbers.append(num)
    num+=0.5
print(numbers)

#Exercise 5:For Loop
#Instructions:
#Write a for loop to print all numbers from 1 to 20, inclusive.
number=()
for number in range(1, 21):
    print(number)
#Write another for loop that prints every number from 1 to 20 where the index is even.
for index, number in enumerate(range(1, 21)):
    if number % 2 == 0:
        print(number)

#Exercise 6:While Loop
#Instructions:
#Write a while loop that keeps asking the user to enter their name
#Stop the loop if the user’s input is your name
name=''
while name !='Maeva':
    name=input('Please enter your name!')
print('That is correct!')

#Exercise 7:Favorite Fruits
#Instructions:
#Ask the user to input their favorite fruits (they can input several fruits, separated by spaces).
#Store these fruits in a list
fruit_input=input('Please enter your favorite fruits: ')
favorite_fruits = fruit_input.split()
print("Your favorite fruits are:", favorite_fruits)
fruit_of_user_input=input('Please enter the name of any fruit!')
if fruit_of_user_input in favorite_fruits:
    print('You chose one of your favorite fruits! Enjoy!')
else:
    print('You chose a new fruit. I hope you enjoy it!')

#Exercise 8:Pizza Toppings
#Write a loop that asks the user to enter pizza toppings one by one.
#Stop the loop when the user types 'quit'.
#For each topping entered, print:
#"Adding [topping] to your pizza."
#After exiting the loop, print all the toppings and the total cost of the pizza.
#The base price is $10, and each topping adds $2.50.
base_price=10
topping_price=2.50
toppings=[]
while True:
    topping=input("Please enter pizza toppings one by one(enter 'quit' if finished): ")
    if topping=='quit':
        break
    print(f"Adding {topping} to your pizza")
    toppings.append(topping)
total_cost=base_price + (topping_price* len(toppings))
print("pizza summary: ")
for item in toppings:
    print(f"{item}")
print(f"Total cost: ${total_cost}")

#Exercise 9:Cinemax Tickets
#Ask for the age of each person in a family who wants to buy a movie ticket.
#Calculate the total cost based on the following rules:
#Free for people under 3.
#$10 for people aged 3 to 12.
#$15 for anyone over 12.
#Print the total ticket cost.
people_under_3=0
people_aged_3_to_12=10
people_over_12=15
total_ticket_cost=0
while True:
    age_input=(input("What's your age?(type 'quit' to finish): "))
    if age_input=='quit':
        break
    family_age=int(age_input)
    if family_age < 3:
        print('Free ticket!')
    elif 3 <= family_age <= 12:
        total_ticket_cost += 10
        print('Ticket $10')
    else:
        total_ticket_cost += 15
        print('Ticket $15')
    print(f"total_ticket_cost: ${total_ticket_cost}")

#Bonus:
#Imagine a group of teenagers wants to see a restricted movie (only for ages 16–21).
#Write a program to:
#Ask for each person’s age.
#Remove anyone who isn’t allowed to watch.
#Print the final list of attendees.
list_allowed=[]
while True:
    age=input("What's your age?(type 'quit' when finished):")
    if age=='quit':
        break
    teenagers=int(age)
    if teenagers <16:
        print("Not allowed!")
    elif teenagers >= 16:
        print("You may go!")
    list_allowed.append(teenagers)
print("Final list of attendees:", len(list_allowed))

#Exercise 10: Sandwich Orders
#Instructions:
#Using the list:
#sandwich_orders = ["Tuna", "Pastrami", "Avocado", "Pastrami", "Egg", "Chicken", "Pastrami"]
#The deli has run out of “Pastrami”, so use a loop to remove all instances of “Pastrami” from the list.
#Prepare each sandwich, one by one, and move them to a list called finished_sandwiches.
#Print a message for each sandwich made, such as: "I made your Tuna sandwich."
#Print the final list of all finished sandwiches.
sandwich_orders = ["Tuna", "Pastrami", "Avocado", "Pastrami", "Egg", "Chicken", "Pastrami"]
finished_sandwiches=[]
print("The deli has run out of 'Pastrami'.")
while "Pastrami" in sandwich_orders:
    sandwich_orders.remove("Pastrami")
for sandwich in sandwich_orders:
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)
print("Final list of all finished_sandwiches:", finished_sandwiches)
