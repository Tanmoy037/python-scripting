# Disk Usage Check:

# Write a Python script that uses the subprocess module to run the df -h command (on Linux or macOS) or wmic logicaldisk get size,freespace,caption (on Windows) to check disk usage.
# Print the output of this command in your Python script.

# Ping Script:

# Write a function ping_host that takes a list of IP addresses and checks if each IP is reachable.
# Use the ping command for this (on Windows, ping -n 1 <IP>; on Linux/macOS, ping -c 1 <IP>).
# Print a message for each IP like "IP <IP> is reachable" or "IP <IP> is not reachable" based on the result.

# Bonus Task (Optional):

# Write a function execute_command(command) that takes a string representing any shell command, runs it, and prints both the output and any errors.
# This function will allow you to automate arbitrary shell commands directly from Python.

# Tips

# Use subprocess.run with capture_output=True and text=True to capture and print the output as text.
# For the ping script, check result.returncode from subprocess.run to determine if the ping was successful (0 means success).
# Test each part individually to ensure it works correctly.
import subprocess

def check_memory():
    result = subprocess.run(["df", "-h"],capture_output=True, text=True)
    print(result.stdout)

check_memory()

def ping_host():
    ip_list = ["8.8.8.8", "8.8.4.4", "192.168.1.1"]
    for i in ip_list:
        result = subprocess.run(["ping","-c", "1", i],capture_output=True, text=True )
        if result.returncode == 0:
            print(f"IP {i} is reachable")
        else:
            print(f"IP {i} is not reachable")

        print(result.stdout)

ping_host()


def execute_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    if result.returncode == 0:
        print("Command Output\n",result.stdout)
    else:
        print("Command Output\n", result.stderr)

execute_command("ls -l")
execute_command("ping -c 1 8.8.8.8")

    



