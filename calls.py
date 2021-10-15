#!usr/bin/env python3
import subprocess as sub
import os
import sys
import glob

def new_file(pad_path):
    print("Chosen option: Create a new file \n")
    new_file_name = input("[+] New file name: ")
    new_file_name = new_file_name + ".txt"
    current_file_path = pad_path + "/" + new_file_name
    print("Creating file: " + new_file_name)
    sub.call(["touch", current_file_path])
    sub.call("clear")
    print("First entry: " + new_file_name)
    os.system(f"cat > {current_file_path}")
    
    
def add_to_file(pad_path):
    print("Chosen option: Add to a file \n\n-* Files:")
    os.system(f"ls -r --format=single-column {pad_path}")
    chosen_file = input("[+] Select file: ")
    sub.call("clear")
    print("Adding to file: " + chosen_file + 
    "\n--------------------------------------------------------------------------------------------")
    current_file_path = pad_path + "/" + chosen_file
    os.system(f"cat >> {current_file_path}")
    
def overwrite_file(pad_path):
    print("Chosen option: Overwrite a file\n\n-* Files:")
    os.system(f"ls -r --format=single-column {pad_path}")
    chosen_file = input("[+] Select file: ")
    sub.call("clear")
    print("Overwriting file: " + chosen_file + 
    "\n--------------------------------------------------------------------------------------------")
    current_file_path = pad_path + "/" + chosen_file
    os.system(f"cat > {current_file_path}")


def read_file(pad_path):
    print("Chosen option: Read a file\n\n-* Files:")
    os.system(f"ls -r --format=single-column {pad_path}")
    chosen_file = input("[+] Select file: ")
    sub.call("clear")
    print("Reading file: " + chosen_file + 
    "\n--------------------------------------------------------------------------------------------")
    current_file_path = pad_path + "/" + chosen_file
    os.system(f"cat {current_file_path}")
    
    
def delete_file(pad_path):
    print("Chosen option: Delete a file\n\n-* Files:")
    os.system(f"ls -r --format=single-column {pad_path}")
    chosen_file = input("[+] Select file: ")
    sub.call("clear")
    print("Deleting file: " + chosen_file)
    current_file_path = pad_path + "/" + chosen_file
    os.system(f"rm {current_file_path}")
    print(f"Chosen file deleted")
