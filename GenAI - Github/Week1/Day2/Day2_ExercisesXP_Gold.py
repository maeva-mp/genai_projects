print("Hello world\nHello world\nHello world\nHello world\nI love python\nI love python\nI love python\nI love python")
month=int(input("Please enter a month number(1to12):"))
if 3 <= month <= 5:
    print("It's Spring")
elif 6 <= month <= 8:
    print("It's Summer")
elif 9 <= month <= 11:
    print("It's Autumn")
elif month== 12 or 1 <= month <= 2:
    print("It's Winter")
else:
    print('Invalid')