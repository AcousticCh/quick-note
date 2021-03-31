#!/usr/bin/env python
import subprocess as sub
import os
import sys
import glob

username = os.getlogin()
notepad_file_path = "/home/" + username + "/Documents/notepad_files"

try:
	os.path.exists(notepad_file_path)
except:
	sub.call(["mkdir", notepad_file_path])
	print("false")

#try:
sub.call("clear")
user_file_call = input("Would you like to:\nCreate a new file? Type \"n\"\nAdd to a file? Type \"a\"\nOverwrite a file? Type \"o\"\nRead a file? Type \"r\"\nDelete a file? Type \"d\"\n[+] Options (n/a/o/r/d): ")
sub.call("clear")
if  user_file_call.upper() == "N":
	print("Chosen option: Create a new file \n")
	new_file_name = input("[+] New file name: ")
	new_file_name = new_file_name + ".txt"
	current_file_path = notepad_file_path + "/" + new_file_name
	print("Creating file: " + new_file_name)
	sub.call(["touch", current_file_path])
	sub.call("clear")
	print("First entry: " + new_file_name)
	os.system(f"cat > {current_file_path}")
	
	#experimenting with add
	
elif user_file_call.upper() == "A":
	print("Chosen option: Add to a file \n\n-* Files:")
	os.system(f"ls -r --format=single-column {notepad_file_path}")
	chosen_file = input("[+] Select file: ")
	sub.call("clear")
	print("Adding to file: " + chosen_file + "\n--------------------------------------------------------------------------------------------")
	current_file_path = notepad_file_path + "/" + chosen_file
	os.system(f"cat >> {current_file_path}")
	
elif user_file_call.upper() == "O":
	print("Chosen option: Overwrite a file\n\n-* Files:")
	os.system(f"ls -r --format=single-column {notepad_file_path}")
	chosen_file = input("[+] Select file: ")
	sub.call("clear")
	print("Overwriting file: " + chosen_file + "\n--------------------------------------------------------------------------------------------")
	current_file_path = notepad_file_path + "/" + chosen_file
	os.system(f"cat > {current_file_path}")
elif user_file_call.upper() == "R":
	print("Chosen option: Read a file\n\n-* Files:")
	os.system(f"ls -r --format=single-column {notepad_file_path}")
	chosen_file = input("[+] Select file: ")
	sub.call("clear")
	print("Reading file: " + chosen_file + "\n--------------------------------------------------------------------------------------------")
	current_file_path = notepad_file_path + "/" + chosen_file
	os.system(f"cat {current_file_path}")
elif user_file_call.upper() == "D":
	print("Chosen option: Delete a file\n\n-* Files:")
	os.system(f"ls -r --format=single-column {notepad_file_path}")
	chosen_file = input("[+] Select file: ")
	sub.call("clear")
	print("Deleting file: " + chosen_file)
	current_file_path = notepad_file_path + "/" + chosen_file
	os.system(f"rm {current_file_path}")
	print(f"Chosen file deleted")
else:
	print("[-] Invalid Input: Please only type given options")
	
		
#except:
	#print("False")
