print("Welcome To Rollercoaster!")
#using the input function to ask for the user height in cm.
height = int(input("Enter your hieght here in cm. \n"))

#using the if, elif and else conditonal statement to check if users are eligible to ride the rollercoaster
age = int(input("How old are you? \n"))
bill = 0
if height > 120:
    print("You are eligible to ride the rollercoaster.")
    if age < 12:
        bill += 5
        print("Children tickets are $5.")
    elif age < 18:
        bill += 7
        print("Youth tickets are $7.")
    elif age > 18:
        bill += 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken, Y or N.")
    if wants_photo == "Y":
        bill += 1

    print(f"Your total bill is ${bill}. Enjoy your ride!")
else:
    print("Sorry, you need to grow taller for you to ride.")

