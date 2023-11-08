#create an input function to ask the user for the number they want to check
number = int(input("Enter the number you want to check here. \n"))

#using the if & else conditional statement to create a condition which check if the number is an odd or even number.
if number % 2 == 0:
    print("This is a even number.")
else:
    print("This is an odd number.")