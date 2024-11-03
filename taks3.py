# Day 3 Assignment: Functions and Modular Code
# Goal:
# Learn to define functions, use arguments and return values, and structure your code in a modular way.

# Instructions:
# Uppercase Server Names:

# Write a function named print_servers_uppercase that takes a list of server names as input.
# The function should print each server name in uppercase.
# Example: If the list is ["server1", "database", "proxy"], the output should be:
#
# SERVER1
# DATABASE
# PROXY

# Prime Checker:
# Write a function named is_prime that takes a single integer as an argument.
# The function should return True if the number is prime and False if it’s not.
# A prime number is only divisible by 1 and itself, so check if any number from 2 to the square root of the number divides it evenly.
# Test your function with numbers like 7 (prime) and 8 (not prime).

# Bonus Task (Optional):
# Reusable Greeting Function:
# Write a function greet_user that takes a username as input and prints a greeting like "Hello, <username>! Welcome back!".
# Call this function with different names to test it.

import math

def print_servers_uppercase(server_names):
    for server in server_names :
        print (server.upper())

servers = ["server1", "database", "proxy"]
print_servers_uppercase(servers)


ef is_prime(num):
    if num < 2:
        return False 
    max_divisor = math.isqrt(num)  
    for i in range(2, max_divisor + 1):
        if (num % i) == 0:
            return False  
    return True 


number = 7
if is_prime(number):
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")


def greet_user(name):
    print ("Hello", name,"! Welcome back!")

greet_user("Tanmoy")