# Day 2 Assignment
# Let’s dive into today’s task on control flow.

# Username and Password Verification Script:

# Define variables username and password with fixed values (e.g., username = "admin", password = "1234").
# Ask the user for their username and password.
# Print “Access Granted” if both match the predefined values, otherwise print “Access Denied.”
# Loop with Conditions:

# Write a for loop that prints numbers from 1 to 10.
# Use an if statement to skip 5 and stop the loop completely at 8.


username = "admin"
password = "1234"

usernameinput = input ("Enter your user name : ")
passwordinput = input ("Enter your password : ")

if (usernameinput == username) and (passwordinput == password):
    print("Access Granted")
else: 
    print("Access Denied")


for i in range(1,11):
    if (i == 5): continue
    if (i == 8): exit()
    print(i)
