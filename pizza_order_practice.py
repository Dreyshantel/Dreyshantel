print("Welcome to pizza order delivery")
size = input("What size of pizza do you want? S, M or L  \n")
add_pepperoni = input("Do you want to add pepperoni? Y or N  \n")
add_cheese = input("Do you want some extra cheese? Y or N \n")

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill +=3

if add_cheese == "Y":
    bill += 1

print(f"your final bill is: ${bill}.")