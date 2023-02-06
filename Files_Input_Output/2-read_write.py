#!/usr/bin/python3

with open("try.txt", "w") as file:
    file.write("My name is Kathy\nI am a beautiful girl\nI am 10 years old and i am in grade 4\nI have a litle dog named Lamla, he is very cute and he was named after my late grandfather")

with open("try.txt") as file1:
    print(file1.read())

print("\n" * 2)

# a code that will print each line, number it, state number of word, number of lenght and average word length
with open ("try.txt") as file3:

    line_num = 1 #sets line number to 1 outside loop

    while True:
        line = file3.readline() #reads a line(first), and eliminates it, next loop sees second line as first

        if not line: #if no line stop the while loop
            break

        print("line",line_num,":",line) #prints the line

        word_num = len(line.split()) #gets number of words byt turning line into a list with split(at every space), and counting length of list

        print(f"Number of words = {word_num}") #shows numbers of words

        letter_num= 0 #sets letter counter to zero out side next loop for counting letters

        for j in line: #loops through content of line, checks for alphabet, if alphabet,counts up letter_num by 1
            if j.isalpha() is True:
                letter_num = letter_num + 1

        print(f"Number of letters = {letter_num}") #print Number of letters

        ave_word_length = letter_num/word_num #find average word length
        

        print(f"Average word length = {ave_word_length:.2}") #prints average word length in float formart at 2 decimal places

        print ("====================================")

        line_num = line_num + 1 # counts line number up

        #codes goes back up the while loop to start again
