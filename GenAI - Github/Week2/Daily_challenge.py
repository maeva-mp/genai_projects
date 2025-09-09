#Daily Challenge : Lists & Strings

#Challenge 1: Multiples of a Number

user_num = int(input("Can you enter a number in integer: "))
user_len = int(input("Can you enter a length in integer: "))

multiples = []

for number in range(1, user_len +1):
     multiples.append(user_num *number )

print("List of multiples:", multiples)


#Challenge 2: Remove Consecutive Duplicate Letters

user_word = input("Enter a string: ") 

result = ""

for letter in user_word:
     if letter != result[-1:]:
          result += letter
print(result)

