import random

names = ['Angel', 'Nikki', 'Mike', 'Victor', 'Ruby']
#get total number of items
num_items = len(names)
# generating a random number for items from 0 to the last index
random_choice = random.randint(0, num_items - 1)
# create a variable for random number
random_name = names[random_choice]
print(f"{random_name} is going to buy the meals.")