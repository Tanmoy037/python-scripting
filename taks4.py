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

from datetime import datetime

# Part 1: Reading from a file
def read_servers():
    # Open the file in read mode
    with open("servers.txt", "r") as file:
        # Read and print each line
        for line in file:
            print(line.strip())  # strip() removes any trailing newline or spaces

# Part 2: Writing to a log file
def log_server_checks():
    # Open the log file in append mode so we add to it without overwriting
    with open("log.txt", "a") as log_file:
        # Open servers.txt and read each server
        with open("servers.txt", "r") as file:
            for line in file:
                server_name = line.strip()  # Remove any trailing newline
                log_entry = f"Checked {server_name}"
                print(log_entry)  # Print to console (for reference)
                log_file.write(log_entry + "\n")  # Write to log file

# Bonus Part: Adding timestamps to the log entries
def log_server_checks_with_timestamp():
    with open("log.txt", "a") as log_file:
        with open("servers.txt", "r") as file:
            for line in file:
                server_name = line.strip()
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                log_entry = f"{timestamp} Checked {server_name}"
                print(log_entry)  # Print to console
                log_file.write(log_entry + "\n")  # Write to log file with timestamp

# Run the functions
read_servers()  # Part 1: Reading and printing servers

# Uncomment one of these based on what you want to run
# log_server_checks()  # Part 2: Writing logs without timestamps
log_server_checks_with_timestamp()  # Part 3: Writing logs with timestamps
