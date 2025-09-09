#Daily challenge GOLD : Happy birthday
# Instructions
# Ask the user for their birthdate (specify the format, for example: DD/MM/YYYY).
# The number of candles on the cake should be the last number of the users age,
# if they are 53, then add 3 candles

from datetime import datetime

birthdate= input("Enter your birthdate (DD/MM/YYYY): ")

birthdate = datetime.strptime(birthdate, "%d/%m/%Y")
today = datetime.today()

age = today.year - birthdate.year

last_digit = int(str(age)[-1])

candles = "i" * last_digit

print()
print(f"      ____{candles}___")
print("     |:H:a:p:p:y:|")
print("   __|___________|__")
print("  |^^^^^^^^^^^^^^^^^|")
print("  |:B:i:r:t:h:d:a:y:|")
print("  |                 |")
print("  ~~~~~~~~~~~~~~~~~~~")

