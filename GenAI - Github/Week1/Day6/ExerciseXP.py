#Exercise 1: Converting Lists into Dictionaries
#Instructions:
#You are given two lists. Convert them into a dictionary where the first list contains the keys and the second list contains the corresponding values
#Lists:
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
my_dict = {}
my_dict = {key: value for key, value in zip(keys, values)}
print(my_dict)

#Exercise 2: Cinemax #2
#Instructions:
#Write a program that calculates the total cost of movie tickets for a family based on their ages.
#Family members’ ages are stored in a dictionary.
#The ticket pricing rules are as follows:
#Under 3 years old: Free
#3 to 12 years old: $10
#Over 12 years old: $15
#Family Data:
family={"rick":43,"beth":13,"morty":5,"summer":8}
person_under_3="free"
person_3_to_12_years_old=10
adult_price=15
total_cost=0

for name, age in family.items():
    if age < 3:
        print(name + ": Ticket's free")
    elif 3 < age < 12:
        print(name + ": Ticket's $10")
        total_cost +=person_3_to_12_years_old
    else:
        print(name + ": Ticket's $15")
        total_cost +=adult_price
print("Total cost for the family is:", "$" + str(total_cost))

#Exercise 3: Zara
#Instructions:
#Create and manipulate a dictionary that contains information about the Zara brand.
#Brand Information:
#name: Zara
#creation_date: 1975
#creator_name: Amancio Ortega Gaona
#type_of_clothes: men, women, children, home
#international_competitors: Gap, H&M, Benetton
#number_stores: 7000
#major_color:
        #France:blue,
        #Spain: red,
        #US: pink, green

#Create a dictionary called brand with the provided data.
brand={
    "name":"Zara",
    "creation_date":1975,
    "creator_name":"Amancio Ortega Gaona",
    "type_of_clothes":"men, women, children, home",
    "international_competitor":"Gap, H&M, Benetton",
    "number_stores":7000,
    "major_color":{
        "France":"blue",
        "Spain": "red",
        "US": "pink, green"
    }
}
print(brand)
#Modify and access the dictionary as follows:
#Change the value of number_stores to 2.
brand["number_stores"]=2

#Print a sentence describing Zara’s clients using the type_of_clothes key.
print("Zara's clients prefer", brand["type_of_clothes"][0],["type_of_clothes"] [1], "and", brand["type_of_clothes"][2], "clothing styles.")
