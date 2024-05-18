# AirBnB Clone Project/
* AirBnB Logo (https://1000logos.net/wp-content/uploads/2023/01/Airbnb-logo.png)
# Description of the Project/
This is the first part of the AirBnB clone project. We worked on the backend while interfacing it with a console application with the help of the cmd module in python.
We stored the Python objects (Data) generated in a json file which can be accessed with the help of the json module in python
# The command interpreter/
The application interface is like the Bash shell only that it has a limited number of accepted commands solely defined for the usage in the AirBnB website.
The command line interpreter acts as the frontend of the web app where users will interact with the backend developed with python programming (OOP).
Some of the commands available are:
* show
* create
* update
* destroy
* count
As part of implementation of the command line interpreter accompanied with the backend and file storage system, the folowing actions can be performed:
* Creating new objects (example: New User or New Place)
* Restoring objects from a file,database…
* Performing operations on objects (example: count, compute stats…)
* Updating the attributes of objects
* Destroying objects

# Installation
Clone the repository of the project from Github containing the simple shell program and all of its dependencies.
"
git clone https://github.com/Fredo200/AirBnB_clone.git
"

>>> /console.py : The main executable of the project, the command interpreter
>>> models/engine/file_storage.py: Class that serialize instances to a JSON file and deserialize JSON file to instances
>>> models/__ init __.py: unique `FileStorage` instance for the application
>>> models/base_model.py: the class that defines all the common attributes or methods for other the classes
>>> models/user.py: User class which inherits from BaseModel 
>>> models/state.py: State class that inherits from BaseMode
>>> models/city.py: City class that inherits from BaseModel
>>> models/amenity.py: Amenity class that inherits from BaseModel
>>> models/place.py: Place class that inherits from BaseModel
>>>models/review.py: Review class that inherits from BaseModel

# How to use
Works in two modes:
*Interactive* and *Non-interactive*
In *Interactive mode* the console displays a prompt(hbnb)indicating that a user can write and execute a command
After the command runs, the prompt appears again wait for new command
This can loop as long as the user does not exit the program
"
$ ./console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
(hbnb) 
(hbnb) quit
$
"
In the *Non-interactive mode* the shell needs to run with a command input passed to its execution so that the command runs as soon as the Shell starts
In this mode no prompt appears and no further inputs are expected from a user
"
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
"
# Format of the Command Input
In order to give commands to the console they will need to be passed through an echo in the case of  *Non-interactive mode*
In the *Interactive Mode* commands need to be typed with a keyboard when the prompt appears and will be identified when enter key is pressed(new line)
As soon as this happens the console attempts to execute the command through several ways or shows an error message if it didn't run successfully
In this mode the console can be exited using *CTRL + D* *CTRL + C* or *quit* or *EOF*
# Arguments
Many commands have different options or arguments which can be used to execute the program
For the Shell to recognize these parameters a user should separate everything with spaces

Example:
"
user@ubuntu:~/AirBnB$ ./console.py
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
user@ubuntu:~/AirBnB$ ./console.py

"
# Available commands and functionality

Command | Description

\*quit/EOF* | Exits/Ends program\
\*Usage* | By itself\
+=========================================+
\*help* | Generates text describing how to use a command\
\*Usage* | By itself -0r- + *help <command\>*\
+=========================================+
\*create* | Creates new instance of a valid "Class" and saves it to the JSON file and prints the "id"
--Valid class are: BaseModel, User, State, City, Amenity, Place, Review\
\*Usage* | *create <class name\>*\
+=========================================+
\*show* | Prints the string representation of an instance based on the class name and "id"\
\*Usage* | *show <class name\> <id\>* -or- **<class name\>.show(<id\>)*\
+=========================================+
\*destroy* | Deletes an instance based on the class name and "id" and update and save the change into a JSON file  |
\*Usage* | *destroy <class name\> <id\>* -or- *<class name>.destroy(<id>)*\
+=========================================+
\*all* | Prints all string representation of all instances based or not on the class name\
\*Usage* | By itself or *all <class name\>* -or- *<class name\>.all()*\
+=========================================+
*update* | Updates an instance based on the class name and "id" by adding or updating attribute and save the changes to a JSON file\
\*Usage* | *update <class name\> <id\> <attribute name\> "<attribute value\>"* -or- *<class name\>.update(<id\>, <attribute name\>, <attribute value\>)* -or- *<class name\>.update(<id\>, <dictionary representation\>)*\
+=========================================+
\*count* | Retrieve the number of instances of a class\
\*Usage* | *<class name\>.count()*\

# Author
Fred Oduor and Gabriel Ntim.
