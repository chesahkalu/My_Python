# Random_python_basics
- Some random beginer python codes, creating and solving problems with basic python algorithms.
- The codes on here are meant to act like a beginer's notes on the basics of python programming.
- They are personal random tasks from different sources during my early days of learning and practicing python programming.
- This README will contain a basic decription of the code content of each file.
- In each file will contain comments like notes  stating the basic description and reason of functions,algorithms and syntax.

## [Beginer_basics](./Beginer_basics/) :
[1-yourname.py](./Beginer_basics/1-yourname.py) : This contains codes describing the various string inputs and outputs, including basic rules on
formating and casting while using `print` functions.

[2-index_slicing.py](./Beginer_basics/2-index_slicing.py) : This provides some of the basic rules on indexing and slicing through basic string variable,
which also works for lists. Also loop through a string as also done in a list, and concantenating new strings into.

[3-simple_calculator.py](./Beginer_basics/3-simple_calculator.py): A simple calculator showing basic oprations;
use of the input function on run, and split funtions during input.
Also shows use of various flow commands such as `if` , `elif`.

[4-fizzbuzz.py](./Beginer_basics/4-fizzbuzz.py): The almighty fizzbuzz. Shows how to loop through a range of numbers and uses flow command to print either
`Fizz` if the number is a multiple of `3`, `Buzz` if it is a multiple of `5` and `Fizzbuzz` if they are multiples of both `3 and 5`.

[5-interest_rate.py](./Beginer_basics/5-interest_rate.py): Calculating and printing interest rate when given initial investment, rate and time.

[6-pine_tree.py](./Beginer_basics/6-pine_tree.py): This code prints a pictorial pine tree using the `#` symbol.
It shows how to manipulate end of lines,spaces and new lines.

[7-string_manipulators.py](./Beginer_basics/7-string_manipulators.py): This conatains a handfull of functions to manipulate strings.

[8-random_list.py](./Beginer_basics/8-random_list.py): This shows usage of the python `random` function in creating a random list of integers.

[9-print_ranging.py](./Beginer_basics/9-print_ranging.py): The `range` function and how it is used.

[10-loop_brk_cnt.py](./Beginer_basics/10-loop_brk_cnt.py): Some code showing the `while true` loop function, including `break` and `continue`.

[11-try_except.py](./Beginer_basics/11-try_except.py): shows how to use the `try except` function.

[12-up_low_case.py](./Beginer_basics/12-up_low_case.py): a code that changes a given string of lowercase letters to uppercase. Intro into `ASCII` keys.

[13-ascii.py](./Beginer_basics/13-ascii.py): some basics about using the ascii keys in string manipulations on python.

[14-cipher](./Beginer_basics/14-cipher.py): This is a function that takes in a given message, and ciphers it to a hidden massage by moving each letter a number
of places ahead. The number of places to be moved becomes the key. ie: if key is 1, letter A becomes letter B.


## [Data_structures](./Data_structures/) :
File containing some valuable basics on various data structures like `lists`,`tuples`,`sets`,`dictionaries`

[1-list.py](./Data_structures/1-lists.py): This file contains some detailed commeents on lissts, its methods and usage.

[2-mutable_tuple.py](./Data_structures/2-mutable_tuple.py): This file contains a function that can change the value in a given index in a tuple.
Normally tupples are immutable. Also are other basics of using a tuple.

[3-set.py](./Data_structures/3-sets.py): This file contains codes describing the use of set data structures as well as most of its functions and methods.

[4-dictionary](./Data_structures/4-dictionary.py): file containing some codes on python dictionaries, with some functions created using dictionary
data structures.

[5-pallindrom.py](./Data_structures/5-palindrome.py): This is a function that checks if a string is the same if read backwards(palindrome).

## [OOP_Objects_Classes](./OOP_Objects_Classes/) : 
File containing basics and codes on Object Oriented Programming. This is one of the most powerful methods of programming. Understanding OOP is encouraged to
become good at programming and Data manipulations. Taking time to understand, recall and practice all the principles and fundamentals of this programming style
is highly adviced.

[1-classes.py](./OOP_Objects_Classes/1-classes.py): file containing various basics about classes, its objects, methods and attribute. This codes contains
lots of comment which might come in handy to better understand Classes.

[2-getters_setters](./OOP_Objects_Classes/2-getters_setters.py): getters and setters are methods in python encapsulation. Encapsulation is basical bonding datas
and methods of the data as a single unit.eg- A Class. This datas and methods can be set to either public or private. And getters and setters are used to access the
datas and change the data respectively if they are set to private. In this code will contain various other magic methods used to make classes more powerful such as 
__str__ and __repr__. The @staticmethod, @classmethods, __del__, and usage of class attributes in methods

[3-inheritance.py](./OOP_Objects_Classes/3-inheritance.py): All about a class inheriting the methods and atttributes of another class.

## [Files_Input_Output](./Files_Input_Output/): 
All about reading , writing and appending text files in UTF-8(Unicode Transformation Format) encoding into files.

[1-intput_output.py](./Files_Input_Output/1-input_output.py): Codes on basics of opening ,reading, writing and closing files.

[2-read_write.py](./Files_Input_Output/2-read_write.py): More indepth on how to write and read files. A code that will print each line, number it, state number of word, number of lenght and average word length

[3-json_parsing.py](./Files_Input_Output/3-json_parsing.py): JSON (JavaScript Object Notation) is a popular data format used for representing structured data. It's common to transmit and receive data between a server and web application in JSON format. Code to parse, read and write JSON in Python. Also, converting JSON to dict and pretty print it.

## [Testing](./Testing/) : Testing codes to ensure they work properly and as intended.

* [Unittesting](./Testing/Unittesting/); Unit tests are segments of code written to test other pieces of code, typically a single function or method, that we refer to as a unit. They are a very important part of the software development process, as they help to ensure that code works as intended and catch bugs early on.Unittest uses methods created in classes to manage tests. It has support for automation, setup, and shutdown code when testing. Unittest has several rich, in-built features that are unavailable in doctest,including generators and group fixture managers like setUp and tearDown.Since unittest follows the object-oriented method,it’s more suitable for testing class-based method
    - [1-max_integer.py](./Testing/Unittesting/1-max_integer.py): This is a code for a function that takes in a list of values and sorts them , then returns the highest
    value. It should work for both integer list and string lists.
    - [1-max_integer_test.py](./Testing/Unittesting/1-max_integer_test.py): This is a unit test file testing every possible scenario for the max_integer fuction codes.

    - [2-customer_class.py](./Testing/Unittesting/2-customer_class.py): This is a class of customers with some attributes and methods.
    - [2-test_customer_class.py](./Testing/Unittesting/2-test_customer_class.py) A test file showing how to unittest a class