#!/usr/bin/python3

with open("try.txt", "w") as file:
    file.write("My name is Kathy\nI am a beautiful girl\nI am 10 years old and i am in grade 4\nI have a litle dog named Lamla, he is very cute and he was named after my late grandfather")

with open("try.txt") as file1:
    print(file1.read())

print("\n" * 2)