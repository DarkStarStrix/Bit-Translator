# make a bit translator to convert words into binary

import os
import platform
# import modules
import sys
import time

# define variables
version = "1.0.0"
version_info = "Bit Translator Version: " + version


# define functions use oop and a reverse function to convert binary to text
class BitTranslator:
    def __init__(self, text):
        self.text = text

    def to_binary(self):
        binary = ' '.join(format(ord(i), 'b') for i in self.text)
        return binary

    def reverse(self):
        text = ''.join(chr(int(x, 2)) for x in self.text.split())
        return text


# define functions
def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


# ask user if they want to translate text to binary or binary to text
def ask():
    print("1. Text to Binary")
    print("2. Binary to Text")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        clear()
        text = input("Enter text to convert to binary: ")
        print(BitTranslator(text).to_binary())
        time.sleep(2)
        clear()
        ask()
    elif choice == "2":
        clear()
        text = input("Enter binary to convert to text: ")
        print(BitTranslator(text).reverse())
        time.sleep(2)
        clear()
        ask()
    elif choice == "3":
        clear()
        print("Exiting...")
        time.sleep(2)
        sys.exit()
    else:
        clear()
        print("Invalid choice")
        time.sleep(2)
        clear()
        ask()


# main function
def main():
    print(version_info)
    print("Welcome to the Bit Translator")
    print("Created by:")
    print(" ")
    ask()


# run main function
if __name__ == "__main__":
    main()
