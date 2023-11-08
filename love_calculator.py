print("Welcome to love calculator!")
name1 = input("What is your name? \n")
name2 = input("What is your name? \n")

#combining the strind using the concatenation method
combined_string = name1 + name2
#using the .lower() method to turn string to lowercase
lower_case_string = combined_string.lower()
#using the count method to count the number of character in a name
l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

#using the count method to count the number of character in a name
t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e
#adding true and love using the concatenation method
lovescores = int(str(true) + str(love))

#making use of the conditional and logical statements and the f string method
if (lovescores <10) or (lovescores >90):
    print(f"your lovescore is {lovescores}, you go together like coke and mentos.")
elif (lovescores >40) or (lovescores <50):
    print(f"your lovescore is {lovescores}, you are alright together.")
else:
    print(f"your lovescore is {lovescore}")

