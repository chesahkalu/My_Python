# Random_python_basics
- Some random beginer python codes, creating and solving problems with basic python algorithms.
- The codes on here are meant to act like a beginer's notes on the basics of python programming.
- They are personal random tasks from different sources during my early days of learning and practicing python programming.
- This README will contain a basic decription of the code content of each file.
- In each file will contain comments like notes  stating the basic description and reason of functions,algorithms and syntax.

## [Beginer_basics](./Beginer_basics/) : This folder contains codes on the basics of python programming. It contains codes on the basic syntax.

[0-hello_world.py](./Beginer_basics/0-hello_world.py) : This contains the basic syntax of python, including the `print` function, comments, and

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

## [Python_Data_Structures](./Python_Data_Structures/): This folder contains codes on various data structures in python. Data structures are a way of organizing and storing data so that it can be accessed and worked with efficiently. There are many different types of data structures, and some are specialized to particular types of data while others are more generally used. In this folder, we will be looking at the most common data structures in Python, including lists, tuples, dictionaries, and sets.

[1-list.py](./Data_structures/1-lists.py): This file contains some detailed commeents on lissts, its methods and usage.

[2-mutable_tuple.py](./Data_structures/2-mutable_tuple.py): This file contains a function that can change the value in a given index in a tuple.
Normally tupples are immutable. Also are other basics of using a tuple.

[3-set.py](./Data_structures/3-sets.py): This file contains codes describing the use of set data structures as well as most of its functions and methods.

[4-dictionary](./Data_structures/4-dictionary.py): file containing some codes on python dictionaries, with some functions created using dictionary
data structures.

[5-pallindrom.py](./Data_structures/5-palindrome.py): This is a function that checks if a string is the same if read backwards(palindrome).

## [OOP_Objects_Classes](./OOP_Objects_Classes/) : File containing basics and codes on Object Oriented Programming. This is one of the most powerful methods of programming. Understanding OOP is encouraged to become good at programming and Data manipulations. Taking time to understand, recall and practice all the principles and fundamentals of this programming style is highly adviced. 

[1-classes.py](./OOP_Objects_Classes/1-classes.py): file containing various basics about classes, its objects, methods and attribute. This codes contains
lots of comment which might come in handy to better understand Classes.

[2-getters_setters](./OOP_Objects_Classes/2-getters_setters.py): getters and setters are methods in python encapsulation. Encapsulation is basically bonding datas
and methods of the data as a single unit.eg- A Class. This datas and methods can be set to either public or private. And getters and setters are used to access the
datas and change the data respectively if they are set to private. In this code will contain various other magic methods used to make classes more powerful such as 
__str__ and __repr__. The @staticmethod, @classmethods, __del__, and usage of class attributes in methods.

[3-inheritance.py](./OOP_Objects_Classes/3-inheritance.py): All about a class inheriting the methods and atttributes of another class.

## [Functions_Modules](./Functions_Modules/) : This folder contains codes on functions and modules. Functions are a fundamental part of any programming language. They allow you to reuse code and write more maintainable programs. In Python, functions are defined using the def keyword. Functions can take parameters (arguments) and may return a value.This codes show how to use functions, importing and modules.Also using *args and **kwargs in [some_functions](./Functions_Modules/some_functions.py)

### [classes](./Functions_Modules/classes/) : This folder contains codes on classes and inheritance,to show how sub class inherits from super class.

- [__init__.py](./Functions_Modules/classes/__init__.py) : The __init__.py files are required to make Python treat directories containing the file as packages.
Typically, __init__.py is empty, but it can be used to configure the package or set the __all__ variable, which controls what symbols are imported when someone uses from package import *.
- [super_class](./Functions_Modules/classes/super_class.py) : a super class , a file containing a parent class that would be imported into [sub_class](./Functions_Modules/classes/sub_class.py). Simply showing that class can be imported also
- [sub_class](./Functions_Modules/classes/sub_class.py) : a sub class. The class containing a sub class of Base class in super_class

- [__init__.py](./Functions_Modules/__init__.py) : The __init__.py files are required to make Python treat directories containing the file as packages.
Typically, __init__.py is empty, but it can be used to configure the package or set the __all__ variable, which controls what symbols are imported when someone uses from package import *.

[some_functions](./Functions_Modules/some_functions.py): This contains various functions and notes on some basic rule, syntax and ways for writing a python
function properly. 

[import_module](./Functions_Modules/import_module.py): This conatains codes importing the functions from [some_functions](./Functions_Modules/some_functions.py)
The codes and comments shows how to use the import method thereby using your functions in other files.

[class_import](./Functions_Modules/class_import.py): showing how class methods can imported and its attribute and methods altered


## [Files_Input_Output](./Files_Input_Output/): All about reading , writing and appending text files in UTF-8(Unicode Transformation Format) encoding into files.

[1-intput_output.py](./Files_Input_Output/1-input_output.py): Codes on basics of opening ,reading, writing and closing files.

[2-read_write.py](./Files_Input_Output/2-read_write.py): More indepth on how to write and read files. A code that will print each line, number it, state number of word, number of lenght and average word length.

[3-json_parsing.py](./Files_Input_Output/3-json_parsing.py): JSON (JavaScript Object Notation) is a popular data format used for representing structured data. It's common to transmit and receive data between a server and web application in JSON format. Code to parse, read and write JSON in Python. Also, converting JSON to dict and pretty print it.

[4.csv.py](./FIles_Input_Output4-csv.py): CSV files store data in a tabular form.


## [Testing](./Testing/) : This folder contains codes on testing. Testing is a very important part of software development. It is the process of running a program or application with the intent of finding errors. It is also known as Debugging. There are two types of testing, manual and automated. Manual testing is done by a human tester, while automated testing is done by a software tool. Automated testing is further divided into unit testing, integration testing, and functional testing. Unit testing is the lowest level of software testing where individual units or components of a software are tested. Integration testing is done to evaluate the interfaces between integrated components or systems. Functional testing is done to evaluate the functionality of a system or its components against the business requirements. In this folder, we will be looking at unittesting and doctest.

* [Unittesting](./Testing/Unittesting/); Unit tests are segments of code written to test other pieces of code, typically a single function or method, that we refer to as a unit. They are a very important part of the software development process, as they help to ensure that code works as intended and catch bugs early on.Unittest uses methods created in classes to manage tests. It has support for automation, setup, and shutdown code when testing. Unittest has several rich, in-built features that are unavailable in doctest,including generators and group fixture managers like setUp and tearDown.Since unittest follows the object-oriented method,it’s more suitable for testing class-based method
    - [1-max_integer.py](./Testing/Unittesting/1-max_integer.py): This is a code for a function that takes in a list of values and sorts them , then returns the highest
    value. It should work for both integer list and string lists.
    - [1-max_integer_test.py](./Testing/Unittesting/1-max_integer_test.py): This is a unit test file testing every possible scenario for the max_integer fuction codes.

    - [2-customer_class.py](./Testing/Unittesting/2-customer_class.py): This is a class of customers with some attributes and methods.
    - [2-test_customer_class.py](./Testing/Unittesting/2-test_customer_class.py) A test file showing how to unittest a class

* [Doctest](./Testing/Doctest/); Python’s standard library comes equipped with a test framework module called doctest. The doctest module programmatically searches Python code for pieces of text within comments that look like interactive Python sessions. Then, the module executes those sessions to confirm that the code referenced by a doctest runs as expected.Additionally, doctest generates documentation for our code, providing input-output examples. Depending on how you approach writing doctests, this can either be closer to either “‘literate testing’ or ‘executable documentation,’. Sometimes, doctests are written with an example of the function and the expected output, but it may be preferable to also include a comment on what the function is intended to do. Including a comment will ensure that you as the programmer have sharpened your goals, and a future person reading the code understands it well. Remember, the future programmer reading the code may very well be you.
    - [1-add_integer.py](./Testing/Doctest/1-add_integer.py): Python function that returns the integer addition
    of two numbers.
    - [1-add_integer.txt](./Testing/Doctest/1-add_integer.txt): A doctest of 1-add_integer function.

    - [2-print_name.py](./Testing/Doctest/2-print_name.py): Python function that prints a name in
    the format `My name is <first_name> <last_name>`.

    - [2-print_name.txt](./Testing/Doctest/2-print_name.txt): A doctest on the 2-print_name function.


## [MySQLdb_SQLAlchemy](./MySQLdb_SQLAlchemy/) :
### [MySQLdb_SQLAchemy](./)

## [Python_Fabric](./Python_Fabric/): Fabric is a powerful Python library and command-line utility that simplifies the use of SSH for tasks related to application deployment or system administration. With Fabric, you can automate repetitive command-line tasks and streamline your workflow, resulting in significant time savings.SSH is used to connect to remote servers and do everything such as initiating a web server.With Fabric, you can perform SSH activities from your local computer.

[fabfile.py](./Python_Fabric/fabfile.py) : A file showing some of the basic commands of fabric. It shows how to connect to a remote server, run commands, upload and download files, and execute tasks in parallel. It also comments on some of the basic syntax of fabric and do's and don'ts.

[pack_for_deploy.py](./Python_Fabric/pack_for_deploy.py) : A file showing how to use fabric to pack a folder for deployment. It shows how to use the local() function to run a command on the local machine that will compress a folder to a single file using the tar command.

[deploy.py](./Python_Fabric/deploy.py) : A file showing how to use fabric to deploy a folder to a remote server. It shows how to use the run() function to run a command on the remote server that will decompress a folder from a single file using the tar command. It also creates a symbolic link to the folder on the remote server.

## [Python_Request_Network](./Python_Request_Network/): This folder contains codes on how to make requests to a server and get responses from it using the requests module. It also contains codes on how to use the urllib module to make requests to a server and get responses from it. This request and response can be in the form of JSON, XML, HTML, etc. The requests module is a simple and elegant Python HTTP library. It provides methods for accessing Web resources via HTTP. It also allows you to access the response data of Python in the same way. The urllib module provides a high-level interface for fetching data across the World Wide Web. It is a package that collects several modules for working with URLs, such as urllib.request for opening and reading URLs, urllib.error containing the exceptions raised by urllib.request, and urllib.parse for parsing URLs. It also contains a subpackage, urllib.robotparser, which can be used to read robots.txt files.

[1_Fetch.py](./Python_Request_Network/1_Fetch.py):


