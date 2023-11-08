#using the print function to print the welcome statement.
print("Welcome to the BMI calculator!")

#creating a variable for height and weight of users.
height = float(input("Enter your height here in cm. \n"))
weight = float(input("Enter your weight here in kg. \n"))

#mathematical calculation of the bmi
bmi = weight / height ** 2

#using the if, elif and else conditional statement
if bmi < 18.5:
    print(f"your bmi is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"your bmi is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"your bmi is {bmi}, you are overweight.")
elif bmi < 35:
    print(f"your bmi is {bmi}, you are obese.")
else:
    print(f"your bmi is {bmi}, you are clinically obese.")