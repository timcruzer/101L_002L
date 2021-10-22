##Tim Cruz
##tcc3t7@umsystem.edu
##CS 101 
##Lab 6 Week 6
##
##PROBLEM: Do Caesar Encryption/Decryption, including cracking a string w/ 
##  unknown Caesar key. 
##  
##Functions needed: 
##  Encrypt(string_text, int_key): Takes a string and integer key, returns 
##  the encryption of the string using that key. Note that for Caesar encryption, 
##  an encryption with key k (k in 1 - 25) is decrypted by doing the same process 
##  with key 26-k. Returns encrypted string using specified key. 
##  
##  Decrypt(string_text, int_key): Decrypts key by calling Encrypt with key 
##    26-int_key and returning the result. Done this way to make for a cleaner
##    breakdown of the problem. Returns decrypted string using specified key. 
##    
##  Crack(string_text): Decrypts a string by repeatedly calling Decrypt with each 
##    possible key (1 to 25) and remembering the one with a letter frequency 
##    closest to English based on counts of E, T, O, A, I, N. Returns tuple: 
##    decrypted string and decryption key. 
##    
##  Get_input(): Interacts with user, gets user choice of '1'-'4' and returns that 
##  value. If user enters anything else, prints brief error message and tries again. 
##  
##  Print_menu(): Prints menu. No user interaction. 
  
################################ 
import string

def encrypt(phrase, key):
    new_phrase = ''
    for char in phrase.upper():
        if char != ' ':
            char = string.ascii_uppercase[((ord(char) - 65) + key) % 26]
        new_phrase += char
    return new_phrase

def decrypt(phrase, key):
    message = encrypt(phrase, (26 - key))
    return message

def get_input():
    user_input = input('Enter your selection ==> ')
    while (user_input != '1') and (user_input != '2') and (user_input != 'Q'):
        print('You must enter 1, 2, or Q.')
        user_input = input('Enter your selection ==> ')
    return user_input

def print_menu():
    print('MAIN MENU:')
    print('1) Encode a string')
    print('2) Decode a string')
    print('Q) Quit')


if __name__ == '__main__':
    while True:
        print_menu()
        choice = get_input()
        print()
        if choice == '1':
            orig_message = input('Enter (brief) text to encrypt: ')
            key = int(input('Enter the number to shift letters by: '))
            new_message = encrypt(orig_message, key)
            print('Encrypted:', new_message)
        elif choice == '2':
            orig_message = input('Enter (brief) text to decrypt: ')
            key = int(input('Enter the number to shift letters by: '))
            new_message = decrypt(orig_message, key)
            print('Decrypted:', new_message)
        else:
            break
        print()