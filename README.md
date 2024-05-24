0x00. AirBnB clone
This a group project that is aimed at deploying on our server a simple copy of the AirBnB website.
-In this project we are to create
- create a data model
- manage objects via console/command interpreter
- store and persist objects to a file (JSON file)
The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”.
The console will be a tool to validate this storage engine. We are going to be able to manage the objects of our project via command interpreter
what's a command interpreter?
A command interpreter is like a shell that we can use to:
- create a new object
- retrieve an object from a file, a database
- Do operations on objects: count, compute stats
- Update attributes of an object
- Destroy an object.
The command interpreter works both in interactive mode and non-intractive mode. It prints a prompt (hbnb) and waits for the user for input.

command and example
1. Run the console - ./console.py
2. Quit the console - (hbnh) quit
3. Display the help or a command - (hbnb) help <command>
Execution
Your shell should work like this in interactive mode:

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
But also in non-interactive mode: (like the Shell project in C)

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
Authors
Georges MBOCK MBOCK
Grace Chidinma Okoha(member) | Emmail: okohagchidinma@gmail.com
