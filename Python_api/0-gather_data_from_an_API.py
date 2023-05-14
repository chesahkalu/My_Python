#!/usr/bin/python3
"""
Uses https://jsonplaceholder.typicode.com along with an employee ID to
return information about the employee's todo list progress
"""

import requests
from sys import argv

if __name__ == '__main__':
    userId = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}". # gets the user with the id passed in, and converts it to json. Verufy is set to false to ignore no ssl certificate
                        format(userId), verify=False).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}". # ?userId= , is used to access a specific key value pair in the data. Todo = all the tasks for the user with the id passed in
                        format(userId), verify=False).json()
    completed_tasks = [] # empty list to store completed tasks
    for task in todo: 
        if task.get('completed') is True:  # use get to access the value of the key "completed". If it is true, add the title of the task to the completed_tasks list
            completed_tasks.append(task.get('title')) # add the title of the task to the completed_tasks list
    print("Employee {} is done with tasks({}/{}):".   # use get to access the value of the key "name" in user, use len to geth length of items in completed_tasks and todo.
          format(user.get('name'), len(completed_tasks), len(todo)))
    print("\n".join("\t {}".format(task) for task in completed_tasks)) # print the tasks in the completed_tasks list, formatted with a tab and a space, using "\n" to join the item in the list, using task as the variable for each item in the list = "\t Task 1\n\t Task 2\n\t Task 3"
    