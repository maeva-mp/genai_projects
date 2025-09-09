#Exercise 1: Concatenate lists
#Instructions:
#Write code that concatenates two lists together without using the + sign.

list1=['hello']
list2=['world']
list3=[]
list3.extend(list1)
list3.extend(list2)
print(list3)
#Exercise 2: Range of numbers
#Instructions:
#Create a loop that goes from 1500 to 2500 and prints all multiples of 5 and 7.
multiples = []
for number in range(1500, 2501):
    if number % 5 == 0 and number % 7 == 0:
        multiples.append(number)
print(multiples)
#Exercise 3: Check the index
#Instructions:
#Using this variable
#names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
#Ask a user for their name, if their name is in the names list print out the index of the first occurence of the name.
#Example: if input is 'Cortana' we should be printing the index 1
ames = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
user_input=input('Please enter your name!')
if user_input == ames:
    print()
