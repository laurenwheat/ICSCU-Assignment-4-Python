#!/usr/bin/env python3

# Created by: Lauren Wheatley
# Created on: May 2021
# This program tells you if your input is a vowel or not


def main():
    # this function tells you if your input is a vowel or not

    letter = input("Enter a letter: ")

    if letter in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
        print("That is always a vowel")
    elif letter in ('y'):
        print("That is sometimes a vowel")
    else:
        print("That is not a vowel")


if __name__ == "__main__":
    main()
