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
    print(code)
# Calculate the frequency of all letters in a piece of text



# Make frequency chart



# Encode/decode a piece of text — atbash is symetrical



# Fetch and return text from a file



# Create a text-based menu system  



# Start up
def main():
    create_code()

main()