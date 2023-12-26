
# AirBnB clone - The console
-----------------------------


The group project is meant to expose us to the following skills:

- How to create a Python package
- How to create a command interpreter in Python using the cmd module
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- How to manage ```datetime```
- What is an ```UUID```
- What is ```*args``` and how to use it
- What is ```**kwargs``` and how to use it
- How to handle named arguments in a function



### Project Desription
----------------------

The project is a full-stack app which consists of the following:

- A console to create and manage objects
- Web static to create of the project frontend
- MySQL storage data storage
- Web framework to make ```HTML``` files dynamic by using objects stored in a file or database
- RESTful API to expose and manipulate all objects stored via a JSON web interface
- Web dynamic to enable loading of objects from the client side using the RESTful API



### Description of the command interpreter:
-------------------------------------------

The command interpreter aka the console is a command line interface similar to a bash shell but it's only limited to creating and managing models for this project.

Some of the commands available to it are:
- create - for creating new objects
- update - for updating objects
- count - for keeping object counts
- show - for displaying objects
- destroy - for deleting objects


### How to start it
-------------------

#### Installation

First, you need to clone this [repository](https://github.com/Kenny15200/AirBnB_clone.git)
Then run the program as decribed below


### How to use it
-----------------

#### Interactive mode

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$

```

#### In non-interactive mode: 

```
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

```

###### All tests should also pass in non-interactive mode: ```$ echo "python3 -m unittest discover tests" | bash```



### Available Commands
----------------------

|**Command**	|	**Description**					|
|---------------|-------------------------------------------------------|
|**quit or EOF**| Exits the program					|
|**help**	| Provides description of how to use a command		|
|**create**	| Creates a new instance of the ```Class``` and saves it (to the JSON file).|
|**show**	| Prints the string representation of an instance based on the class name and ```id```|
|**destroy**	| Deletes an instance based on the class name and id (saves the change into a JSON file).|
|**all**	| Prints all string representation of all instances based or not on the class name.|
|**update**	| Updates an instance based on the class name and ```id``` by adding or updating attribute (saves the changes into a JSON file).|
|**count**	| Retrieves the number of instances of a class.		|



## Authors
----------

- **Kehinde Opaleye** - [Kenny15200](https://github.com/kenny15200)
- **Bonaventure Anselm** - [bona-anselm](https://github.com/bona-anselm)
