#!/usr/bin/env python
import subprocess as sub
import os
import sys
import glob
from calls import *
username = os.getlogin()
notepad_file_path = "/home/" + username + "/Documents/notepad_files"

path_test = os.path.exists(notepad_file_path)

if path_test == True:
    os.path.exists(notepad_file_path)
else:
    sub.call(["mkdir", notepad_file_path])
    print("false")


sub.call("clear")
user_file_call = input(
"Would you like to:\nCreate a new file? Type \"n\"\nAdd to a file? Type \"a\"\nOverwrite a file? Type \"o\"\nRead a file? Type \"r\"\nDelete a file? Type \"d\"\n[+] Options (n/a/o/r/d): ")
sub.call("clear")
if  user_file_call.upper() == "N":
    new_file(notepad_file_path)
	
elif user_file_call.upper() == "A":
    add_to_file(notepad_file_path)
	
elif user_file_call.upper() == "O":
    overwrite_file(notepad_file_path)
    
elif user_file_call.upper() == "R":
    read_file(notepad_file_path)
    
elif user_file_call.upper() == "D":
    delete_file(notepad_file_path)
else:
    print("[-] Invalid Input: Please only type given options")
	
		
