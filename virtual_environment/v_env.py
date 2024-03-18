"""

The main purpose of using a virtual environment in local development, especially for Python and Django applications, 
is to create an isolated space on your computer for Python projects. 
This isolation allows you to work on multiple projects with different dependencies at the same time without conflicts. 
Here’s a detailed explanation and some instances to illustrate the concept better:

Isolation:
Prevents Dependency Conflicts: Each project can have its own dependencies, or even the same dependencies but in different versions, without interfering with each other. For example, if one project requires Django 2.2 but another needs Django 3.1, virtual environments ensure these requirements don't clash.
Instances of Changes in Virtual Environments

File Changes:
Changes you make to files (your code) are not limited to the virtual environment. These changes are made to the project files themselves, which are not part of the virtual environment. The virtual environment is primarily for Python packages, not your source code.
Package Installations: When you install a package using pip while a virtual environment is activated, the package is installed only within that virtual environment. This is crucial for maintaining the project’s requirements independent of other projects. For instance, installing requests in one virtual environment does not make it available in another.
"""


# Creating a Virtual Environment
# To create a virtual environment, you need to have Python installed on your system.
# If you have Python installed, you can create a virtual environment using the following command:
# python3 -m venv venv

# The first python3 is the Python interpreter you want to use to create the virtual environment.
# The -m venv is a built-in module that comes with Python 3.3 and later versions.
# The venv is the name of the directory where the virtual environment files are stored.


# The command python3 -m venv venv creates a new directory called venv where the virtual environment files are stored.
# The venv directory is created in the current working directory.
# The virtual environment directory contains a copy of the Python interpreter, a copy of the standard library, and other supporting files.

# TO ACTIVATE THE VIRTUAL ENVIRONMENT
# source venv/bin/activate
# The source command runs the activate script in the venv/bin directory. This script activates the virtual environment.
# Once the virtual environment is activated, the command prompt changes to show the name of the activated virtual environment.  
# For example, the command prompt might change from $ to (venv) $ to indicate that the virtual environment is active.

# TO DEACTIVATE THE VIRTUAL ENVIRONMENT
# deactivate
# The deactivate command deactivates the virtual environment. The command prompt changes back to the original state.
