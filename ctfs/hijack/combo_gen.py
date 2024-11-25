# This is a little script used in CTF 'tryhackme hijack' to convert a list of usernames and passwords to bs64 and print this new list to a file

import argparse
import base64
import hashlib

parser = argparse.ArgumentParser()

parser.add_argument("-f", "--file")
parser.add_argument("-u", "--username") 

args = parser.parse_args()

def main():

    combo = read_file()
    
    # plaintext passwords
    #print("PASSWORDS: %s" % combo)

    combo = hash_password_add_username(combo)

    #print("HASHED PASSWORDS: %s" % combo)

    combo = convert_to_bs64(combo)

    #print("B64 PASSWORDS: %s" %  combo)
    
    write_file(combo)

def read_file():
    my_list = []

    with open(args.file, 'r') as file:
        for lines in file:
            my_list.append(lines.strip())
    return my_list

def write_file(my_list):
    with open("bs64_combo_list_output.txt", 'w') as output_file:
        for line in my_list:
            output_file.write("".join(line) + "\n")

def hash_password_add_username(passwords_to_hash):
    hashed_passwords = []

    for x in passwords_to_hash:
        hasher = hashlib.md5()

        hasher.update(x.encode())

        hashed_passwords.append(args.username + ":" + hasher.hexdigest())

    return hashed_passwords


def convert_to_bs64(list_to_encode):
    encoded_list = []

    for x in list_to_encode:
        encoded_list.append(base64.b64encode(x.encode()).decode())

    return encoded_list

main()
