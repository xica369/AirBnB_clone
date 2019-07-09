# 0x00. AirBnB clone - The console

## Description
This console allows to the users, manage the entities of the system using the commands explained in this manual.

The users like the administrator of the app Airbnb clone has the posibility of the manipulate objects and data of the application, this objects are:
 
 * Users
 * Places
 * States
 * Cities
 * Amenities
 * Reviews
 
 
 ## Installation
 
 For use this console you need to have:
 * Linux ubuntu 14.04.3 LTS or higger
 * Python 3.7 or higger

## How to start
You need clone this project on your computer, then, inside of the folder AirBnB clone, type this command

```bash
$./console.py
```
You see the prompt awaiting for type a command:

```bash
(hbnb)
```

The command help show the available commands for this console, type this:

```bash
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
```

## How to use the console
The command line interpreter intialize when you type ./console.py see above.

Exits two ways for you type a command in the console, they are:

1-
````bash
COMMAND Class [ID] [PARAMETERS]
````

2- 
```bash
Class.COMMAND([ID], [PARAMETERS])
```

#Examples:

```bash
(hbnb) Show User 49faff9a-6318-451f-87b6-910505c55907
[User] (246c227a-d5c1-403d-9bc7-6a47bb9f0f68) {'first_name': 'Betty', 'last_name': 'Holberton', 'created_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611352), 'updated_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611363), 'password': '63a9f0ea7bb98050796b649e85481845', 'email': 'airbnb@holbertonshool.com', 'id': '246c227a-d5c1-403d-9bc7-6a47bb9f0f68'}
(hbnb)
```

```bash
(hbnb) User.show(49faff9a-6318-451f-87b6-910505c55907)
[User] (246c227a-d5c1-403d-9bc7-6a47bb9f0f68) {'first_name': 'Betty', 'last_name': 'Holberton', 'created_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611352), 'updated_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611363), 'password': '63a9f0ea7bb98050796b649e85481845', 'email': 'airbnb@holbertonshool.com', 'id': '246c227a-d5c1-403d-9bc7-6a47bb9f0f68'}
(hbnb)

```

The command available for this console are:
* create: Allows to the user, create a instance of the class and print the id.

SYNOPSIS
	create [CLASS NAME]

create Class

Messages:

a) If the class name is missing, print ** class name missing ** (ex: $ create)
b) If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ create MyModel)

example:

```bash
(hbnb) create User
246c227a-d5c1-403d-9bc7-6a47bb9f0f68
(hbnb)
```

* show: Allows to the user, see the information about the ID searched.

SYNOPSIS
	show [CLASS NAME] [ID]

show Class ID

Messages:

a) If the class name is missing, print ** class name missing ** (ex: $ show)
b) If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ show MyModel)
c) If the id is missing, print ** instance id missing ** (ex: $ show BaseModel)
d) If the instance of the class name doesn’t exist for the id, print ** no instance found ** (ex: $ show BaseModel 121212)


example:

```bash
(hbnb) Show User 49faff9a-6318-451f-87b6-910505c55907
[User] (246c227a-d5c1-403d-9bc7-6a47bb9f0f68) {'first_name': 'Betty', 'last_name': 'Holberton', 'created_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611352), 'updated_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611363), 'password': '63a9f0ea7bb98050796b649e85481845', 'email': 'airbnb@holbertonshool.com', 'id': '246c227a-d5c1-403d-9bc7-6a47bb9f0f68'}
(hbnb)
```

* destroy: allow to the user, deletes an instance based on the class name and id.

SYNOPSIS
	destroy [CLASS NAME] [ID]

destroy Class ID

Messages:

a) If the class name is missing, print ** class name missing ** (ex: $ destroy)
b) If the class name doesn’t exist, print ** class doesn't exist ** (ex:$ destroy MyModel)
c) If the id is missing, print ** instance id missing ** (ex: $ destroy BaseModel)
d) If the instance of the class name doesn’t exist for the id, print ** no instance found ** (ex: $ destroy BaseModel 121212)

```bash
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
```

* all: Prints all string representation of all instances based or not on the class name.

SYNOPSIS
	all
	all [CLASS NAME]

all BaseModel or all

Messages:

a) The printed result must be a list of strings (like the example below)
b) If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ all MyModel)

example:

```bash
(hbnb) all BaseModel
["[BaseModel] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 'created_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639717), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639724)}", "[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}"]
(hbnb)
```

* update: Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). Ex: $ update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com".

update <class name> <id> <attribute name> "<attribute value>"
Class.update("[id]", {attribute: value})

Rules:
- Only one attribute can be updated at the time
- You can assume the attribute name is valid (exists for this model)
- The attribute value must be casted to the attribute type
- All other arguments should not be used (Ex: $ update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com" first_name "Betty" = $ update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com")

Messages:

a) If the class name is missing, print ** class name missing ** (ex: $ update)
b) If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ update MyModel)
c) If the id is missing, print ** instance id missing ** (ex: $ update BaseModel)
d) If the instance of the class name doesn’t exist for the id, print ** no instance found ** (ex: $ update BaseModel 121212)
e) If the attribute name is missing, print ** attribute name missing ** (ex: $ update BaseModel existing-id)
f) If the value for the attribute name doesn’t exist, print ** value missing ** (ex: $ update BaseModel existing-id first_name)

example:

```bash
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
(hbnb)
(hbnb) User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", {'first_name': "John", "age": 89})
(hbnb) 
(hbnb) User.show("38f22813-2753-4d42-b37c-57a17f1e4f88")
[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'age': 89, 'first_name': 'John', 'last_name': 'Holberton', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'updated_at': datetime.datetime(2017, 9, 28, 21, 17, 10, 788143), 'password': 'b9be11166d72e9e3ae7fd407165e4bd2', 'email': 'airbnb@holbertonshool.com', 'id': '38f22813-2753-4d42-b37c-57a17f1e4f88'}
```

* count: count the objects taht exists of the class name.

Class.count()

example:


```bash
(hbnb) User.count()
2
(hbnb) 
```

## AUTHORS
 
* **Ximena Carolina Andrade Vargas** - [xica369](https://github.com/xica369)
* **Yony Brinez Valderrama** - [arleybri18](https://github.com/arleybri18)
