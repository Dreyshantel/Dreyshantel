print("Welcome to leap year calculator.")
#use the input function to collect data about the year the user wants to check
year = int(input("What year do you want to check? " ))

#making use of the modulo, if and else conditional statement.
if year % 4 == 0:
    print("A leap year.")
    if year % 100 == 0:
        print("Not a leap year.")
        if year % 400 == 0:
            print("A leap year.")
        else:
            print("Not a leap year.")
    else:
        print("A leap year.")
else:
    print("Not a leap year.")