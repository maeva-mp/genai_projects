#Ask for User Input:
#The string must be exactly 10 characters long.
user_input=input("insert a string(exactly 10 characters): ")
#Check the Length of the String:
#If the string is less than 10 characters, print: "String not long enough."
#If the string is more than 10 characters, print: "String too long."
#If the string is exactly 10 characters, print: "Perfect string" and proceed to the next steps.
if len(user_input) < 10:
    print("String not long enough.")
elif len(user_input) > 10:
    print("String too long")
else:
    print("Perfect string")
#Print the First and Last Characters:
#Once the string is validated, print the first and last characters.
print("First character:", user_input[0])
print("Last character:", user_input[-1])
