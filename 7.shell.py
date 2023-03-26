# -*- coding: utf-8 -*-

# CLAIM: This code is written by myself, 
# with the help of the internet about subprocess and shutil use (but not from other students).
# I started to write this code from Wednesday, 22 March 2023, 4:31 PM.
# and the last modified is at the time I commit all.
# I was not understand about IO redirection, so I have to search on the internet.
# The PIPE was inspired by Mr. "Teacher that did not check my code in the last session" :(((
# (actually, I did not understand about pipe lol)

# Update: After the last tutorial session, Mr.Hiep told me that I can't use "shell = True" in subprocess.call()
# So I have to change the code to use "shell = False"
# and use "shutil.which()" to check if the command is available or not.
# Thanks Mr.Hiep for your suggestion. And now I do understand about pipe (maybe?)!
# May the Buddha bless you and me.

#                            _
#                         _ooOoo_
#                        o8888888o
#                        88" . "88
#                        (| -_- |)
#                        O\  =  /O
#                     ____/`---'\____
#                   .'  \\|     |//  `.
#                  /  \\|||  :  |||//  \
#                 /  _||||| -:- |||||_  \
#                 |   | \\\  -  /'| |   |
#                 | \_|  `\`---'//  |_/ |
#                 \  .-\__ `-. -'__/-.  /
#               ___`. .'  /--.--\  `. .'___
#            ."" '<  `.___\_<|>_/___.' _> \"".
#           | | :  `- \`. ;`. _/; .'/ /  .' ; |
#           \  \ `-.   \_\_`. _.'_/_/  -' _.' /
# ===========`-.`___`-.__\ \___  /__.-'_.'_.-'================
# THIEN TAI - THIEN TAI   `=--=-'        THIEN TAI - THIEN TAI
#        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#              Phật phù hộ, không bao giờ BUG
#            Nguyễn Quang Minh - ICT - BI12-271
#        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import subprocess
import os
import shutil
clear = lambda: os.system("clear")


# Define a function to execute a single command and return the output
def execute_command(command, input_data=None):
    try:
        # Split the command and get the command name
        command_parts = command.split()
        command_name = command_parts[0]
        
        # Check if the command is 'cd'
        if command_name == 'cd':
            # Change the directory to the specified path
            os.chdir(' '.join(command_parts[1:]))
            return ''
        else:
            # Check if the command is in the forbidden commands list
            command_path = shutil.which(command_name)
            if not command_path:
                print(f"{command_name}: command not found")
                return ""
            elif os.path.basename(command_path) in os.environ.get("FORBIDDEN_COMMANDS", "").split(":"):
                print(f"{command_name}: command is forbidden")
                return ""
            else:
                result = subprocess.run(command_parts, shell=False, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, input=input_data)
                return result.stdout.decode().strip()
    except subprocess.CalledProcessError as e:
        print("Error:", e.stderr.decode().strip())
        return ""
    

# Define a function to handle commands with pipes
def execute_piped_command(command):
    # Split the command into separate commands
    commands = command.split("|")
    # Execute the first command with no input
    input_data = None
    output = execute_command(commands[0], input_data)
    # Execute the remaining commands with the output of the previous command as input
    for cmd in commands[1:]:
        input_data = output.encode()
        output = execute_command(cmd, input_data)
    # Return the final output
    return output

clear()

print("Welcome to the $_hell by Nguyen Quang Minh - BI12-271")
print("-----------------------------------------------------")
while True:
    # Read input from user
    command = input(f"$_hell at {os.getcwd()} --> ")
    print("-----------------------------------------------------")

    # Check exit
    if command == "exit":
        break

    # Check IO redirection
    input_file = None
    output_file = None

    # Check for input redirection
    if "<" in command:
        command, input_file = command.split("<")
        input_file = input_file.strip()
        print("Inputed file:", input_file)

    # Check for output redirection
    if ">" in command:
        command, output_file = command.split(">")
        output_file = output_file.strip()
        print("Outputed file:", output_file)

    # Execute command
    if "|" in command:
        result = execute_piped_command(command)
    else:
        result = execute_command(command)

    if output_file:
        with open(output_file, "w") as f:
            f.write(result)
    else:
        print(result)