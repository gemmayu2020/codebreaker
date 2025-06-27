#!/bin/python3
from pygal import Bar
from frequency import english

# Set up data structures 
alphabet = list(" abcdefghijklmnopqrstuvwxyz ")
code={}

# Create the atbash code by reversing the alphabet
def create_code():
    backwards = list(reversed(alphabet))
  
    for i in range(len(alphabet)):
        code[alphabet[i]] = backwards[i]
    #print(code)
# Calculate the frequency of all letters in a piece of text



# Make frequency chart



# Encode/decode a piece of text — atbash is symetrical
def atbash(text):
    text = text.lower()
    output=""
    
    for letter in text:
        if letter in code:
            output +=code[letter]
    return output


# Fetch and return text from a file
def get_text(filename):
    with open (filename) as f:
        text = f.read().replace("/n","")

    return text


# Create a text-based menu system  
def menu():
    choice = " "

    while choice != "c" and choice != "f":
        choice = input("Enter c to encode/decode some text or enter f to perfom some frequency analysis: ")

    if choice == "c":
        print("Running message from cypher....")
        message=get_text("input.txt")
        ""
        code=atbash(message)
        print(code)
# Start up
def main():
    create_code()
    #print(atbash("Test"))
    menu()

main()