# Error Handling with try-except:

# Write a function read_file(filename) that:
# Tries to open a file and read its contents.
# If the file doesn’t exist, catches the error and prints a message like "File not found: <filename>".
# Otherwise, it should print the file’s content.
# Test this function by passing both an existing filename and a non-existing filename to verify the error handling.


# Implementing Logging:

# Create a script that uses Python’s logging module to log messages.
# Configure logging to write to a file named script.log, with the following settings:
# Logging Level: Set to INFO (you'll log informational messages as well as errors).
# Log format should include the time, log level, and message.
# Inside read_file(filename), log each attempt to read a file and log an error if the file isn’t found.

# Bonus Task (Optional):

# Modify the execute_command(command) function from the previous assignment to include logging.
# Log each command run and log errors if any command fails.

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"File not found: {filename}")



import logging

# Configure logging
logging.basicConfig(
    filename='script.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Enhanced read_file function with logging
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(content)
            logging.info(f"Successfully read file: {filename}")
    except FileNotFoundError:
        logging.error(f"File not found: {filename}")
        print(f"File not found: {filename}")

import subprocess

def execute_command(command):
    # Log the command being executed
    logging.info(f"Running command: {command}")
    
    # Run the command
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    # Check if the command was successful
    if result.returncode == 0:
        print("Command Output:\n", result.stdout)
        logging.info(f"Command succeeded: {command}")
    else:
        print("Command Error:\n", result.stderr)
        logging.error(f"Command failed: {command} - Error: {result.stderr}")

# Example usage
read_file("existing_file.txt")        # Test with a file that exists
read_file("nonexistent_file.txt")     # Test with a file that doesn't exist
execute_command("ls -l")              # Example command for Unix
