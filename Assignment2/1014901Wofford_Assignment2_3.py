# CPSC-442-11/Python  - Assignment 2 Problem 3
# Author:  Wofford, Juana 1014901
#
# function to return the morse code for a word
# -----------------------------------------
# morse code alphabet mapping dictionary
morse_alphabet_dictionary = {
    'a': '.-','b': '-...','c': '-.-.','d': '-..',
    'e': '.','f': '..-.','g': '--.','h': '....',
    'i': '..','j': '.---','k': '-.-','l': '.-..',
    'm': '--','n': '-.', 'o': '---','p': '.--.',
    'q': '--.-','r': '.-.','s': '...','t': '-',
    'u': '..-','v': '...-','w': '.--','x': '-..-',
    'y': '-.--','z': '--..'}
#
# the characters of the string (word_entered) is compared
# to each key in the morse alphabet dictionary
# if the key is found in the text string the value is
# placed into a list that is printed to display the
# word in morse code

def word_to_morse(word_entered):
    morse_code_list = []
    for each_character in word_entered:
        for morse_key, morse_values in morse_alphabet_dictionary.items():
            if each_character == morse_key:
                morse_code_list.append(morse_values)

    morse_code_string =''.join(morse_code_list)
    print('Input: ', word_entered)
    print('Output: ', morse_code_string)


# prompt for word, pass word entered to function
word_entered = input("Enter A Word, it will be turned into Morse Code: ")
w = word_to_morse((word_entered))   #call the function to convert word to morse code