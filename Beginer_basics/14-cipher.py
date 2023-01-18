#!/usr/bin/python3

#this is a simple program that will code change a written massage to different letterss with a given key.
#The key shift the letters by the given number of positions.
#also will be writtten as a function, that can be imported in another function or used in the code.
#the usagee of this function can be seen in the function file
def cipher(message, key):
    for i in message:
        if ord(i) >= 65 and ord(i) <= 90: #checks for uppercase letter, to maintain uppercase
            i = chr(ord(i) + key) #inputs key to cipher and move the letters in key number position
            if ord(i) > 90: #if key ciphers above ascii valu of Z, result wont rotate to continue from A 
                i = chr(ord(i) - 26) # Rotates to start from begining A, instead of continue to take next ASCII value
            print(i, end='')
        
        elif ord(i) >= 97 and ord(i) <= 122:#checks if lowercase letter to maintain
            i = chr(ord(i) + key)
            if ord(i) > 122:
                i = chr(ord(i) - 26)
            print(i, end='')

        else:
            print(i, end='')

cipher(input("Please input message to cipher : "), int(input("Please input key: ")))

    