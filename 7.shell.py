# -*- coding: utf-8 -*-

# CLAIM: This code is written by myself, 
# with the help of the internet about subprocess use (but not from other students).
# I started to write this code from Wednesday, 22 March 2023, 4:31 PM.
# and the last modified is at the time I commit all.
# I was not understand about IO redirection, so I have to search on the internet.
# The PIPE was inspired by Mr. "Teacher that did not check my code in the last session" :(((
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
clear = lambda: os.system("clear")

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
    try:
        if input_file:
            with open(input_file, "r") as f:
                stdin = f.read()
                result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, input=stdin)
        else:
            result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        if output_file:
            with open(output_file, "w") as f:
                f.write(result.stdout)
        else:
            print(result.stdout)

    except subprocess.CalledProcessError as e:
        print("Error:", e.stderr)
