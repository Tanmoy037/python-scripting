# Reading from a File:

# Create a text file named servers.txt with the following content (one server per line):
# server1
# server2
# database
# proxy
# Write a script named read_servers.py that opens this file, reads each line, and prints it.
# Writing to a Log File:

# In your script, add functionality to log each server's name to a new file, log.txt, along with the message "Checked <server_name>".
# This log file should append a new line each time the script is run, rather than overwriting the file.
# Example of log.txt output after one run:
# Copy code
# Checked server1
# Checked server2
# Checked database
# Checked proxy
# Bonus Task (Optional):

# Extend your script to add a timestamp to each log entry in log.txt. You can use Python’s datetime module to add the current date and time for each line.
# Example:

# 2023-01-01 10:00:00 Checked server1
# 2023-01-01 10:00:00 Checked server2

# Tips:
# Use the open() function with modes:
# "r" for reading
# "a" for appending (to add to the file without overwriting)
# with open(...) as file ensures the file is properly closed after reading or writing.
# Use datetime.datetime.now() for timestamps.