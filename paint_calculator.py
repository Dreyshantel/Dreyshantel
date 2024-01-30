print("Welcome to paint calculator!")
# import math module
import math
# define a paint calculator function with input that take in height, width and cover as parameters
def paint_calc(height, width, cover):
    area = height * width
    num_of_can = math.ceil(area / cover)
    print(f"You will need {num_of_can} cans of paint.")

# create an input function for wall height and width & call function
test_h = int(input("height of wall: "))
test_w = int(input("width of wall: "))
coverage = 5
paint_calc(height= test_h, width= test_w, cover = coverage)