# Function to check if a number provided by the user is a prime number.

import math

def prime_checker(is_it):
    is_prime = True
    for i in range(2,is_it):
        if is_it % i == 0:
            is_prime = False

    if is_prime:
        print("It's a prime number")
    else:
        print("It's not a prime number.")   


is_it = int(input("Please enter a number: "))




prime_checker(is_it)