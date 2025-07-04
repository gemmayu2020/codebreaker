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
def frequency(text):
    text = list(text.lower())

    freq = {}
    for letter in alphabet:
        freq[letter] = 0

    total_letters = len(text)

    for letter in text:
        if letter in freq:
            freq[letter]+=1

    for letter in freq:
        freq[letter] = freq[letter] / total_letters * 100

    return freq        


# Make frequency chart
def make_chart(text, language):
    chart = Bar(width = 800 ,height = 400, title="Frequency Analyser", x_labels = list(text.keys()))
    chart.add("Target message", list(text.values()))
    chart.add("Language", list(language.values()))

    chart.render()

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

    elif choice == "f":
        print("Analysing that message.....")
        message=get_text("longer.txt")
        message_freq=frequency(message)
        #print(message_freq)
        lang_freq = english
        make_chart(message_freq, lang_freq)
# Start up
def main():
    create_code()
    #print(atbash("Test"))
    menu()

main()