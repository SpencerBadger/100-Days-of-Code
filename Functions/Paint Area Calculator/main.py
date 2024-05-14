## Paint Area Calculator Function
import math

def paint_area_calculator(height,width, coverage):
    num_cans = ((height*width) / coverage)
    round_up_cans = math.ceil(num_cans)
    print(f"You will need {round_up_cans} cans of paint")

height = int(input("Input your height: "))
width = int(input("Input your width: "))
coverage = 5



paint_area_calculator(height,width,coverage)