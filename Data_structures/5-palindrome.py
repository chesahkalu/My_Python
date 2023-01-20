#!/usr/bin/python3

def check_palindrome(x):

    x_list=[]

    for i in x:
        x_list.append(i)
    
    x_list_cp = x_list.copy()

    x_list_cp.reverse()
    

    if x_list_cp == x_list:
        print(x, ", is a palindrome, it reads the same from backward")
    else:
        print(x, ", is not a palindrome. It doesnt read the same from backward")
        
check_palindrome("radar")
check_palindrome("hope")
check_palindrome("madam")