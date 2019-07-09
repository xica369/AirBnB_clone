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
* create:
	create Class
Allows to the user, create a instance of the class and print the id.

example:

```bash
(hbnb) create User
246c227a-d5c1-403d-9bc7-6a47bb9f0f68
(hbnb)
```

* show:
	show Class ID
Allows to the user, see the information about the ID searched.

example:

```bash
(hbnb) Show User 49faff9a-6318-451f-87b6-910505c55907
[User] (246c227a-d5c1-403d-9bc7-6a47bb9f0f68) {'first_name': 'Betty', 'last_name': 'Holberton', 'created_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611352), 'updated_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611363), 'password': '63a9f0ea7bb98050796b649e85481845', 'email': 'airbnb@holbertonshool.com', 'id': '246c227a-d5c1-403d-9bc7-6a47bb9f0f68'}
(hbnb)
```



 
* **Ximena Carolina Andrade Vargas** - [xica369](https://github.com/xica369)
* **Yony Brinez Valderrama** - [arleybri18](https://github.com/arleybri18)
