#!/usr/bin/python3

def check_palindrome(x): #defines a function, that will take a string variable as X and check if it is a palindrome

    x_list=[] #to use some methods like reeverse and split, the string has to be turned to a list. Empty list created

    for i in x:
        x_list.append(i) #each character in string x is appended into x_list, making a list of each string character
    
    x_list_cp = x_list.copy()#to reverse the list, the list reversed becomes the same list, so a copy is made to keep the first list

    x_list_cp.reverse()#list copy reversed
    

    if x_list_cp == x_list: #checks if original list and reversed list are the same
        print(x, ", is a palindrome, it reads the same from backward")
    else:
        print(x, ", is not a palindrome. It doesnt read the same from backward")
        
check_palindrome("radar")
check_palindrome("hope")
check_palindrome("madam")