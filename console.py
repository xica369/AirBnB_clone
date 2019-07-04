#!/usr/bin/python3
"""Class HBNBComand that contains the entry point
of the command interpreter
"""
import cmd
import shlex
from models import base_model, storage, user, place, state, city, amenity
from models import review
from models.engine import file_storage

BaseModel = base_model.BaseModel
FileStorage = file_storage.FileStorage
User = user.User
Place = place.Place
State = state.State
City = city.City
Amenity = amenity.Amenity
Review = review.Review
NClass = ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]


class HBNBCommand(cmd.Cmd):
    """ Command Interpreter
    """
    prompt = "(hbnb) "

    def do_EOF(self, args):
        """EOF command to exit the program
        """
        return(True)

    def do_quit(self, args):
        """Quit command to exit the program
        """
        return(True)

    def emptyline(self):
        """It does not perform any action
        """
        pass

    def do_create(self, args):
        """create: Creates a new instance of BaseModel,
        saves it (to the JSON file)
        and prints the id. Ex: $ create BaseModel
        If the class name is missing, print ** class name missing **
        If the class name doesnt exist, print ** class doesn't exist **
        """
        arguments = shlex.split(args)
        if len(arguments) == 0:
            print("** class name missing **")
        elif len(arguments) == 1 and arguments[0] in NClass:
            new_base_model = eval(arguments[0])()
            new_base_model.save()
            print("{}".format(new_base_model.id))
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """show: Prints the string representation of an instance
        based on the class name and id.
        Ex: $ show BaseModel 1234-1234-1234
        If the class name is missing, print ** class name missing **
        If the class name doesnt exist, print ** class doesn't exist **
        If the id is missing, print ** instance id missing **
        If the instance of the class name doesnt exist for the id,
        print ** no instance found **
        """
        arguments = shlex.split(args)
        if len(arguments) == 0:
            print("** class name missing **")
        elif len(arguments) >= 1 and arguments[0] not in NClass:
            print("** class doesn't exist **")
        elif len(arguments) == 1 and arguments[0] in NClass:
            print("** instance id missing **")
        else:
            flag = 0
            dic = storage.all()
            for key, value in dic.items():
                _id = key.split(".")[1]
                if _id == arguments[1]:
                    flag = 1
                    print(value)
                    break
            if flag == 0:
                print("** no instance found **")

    def do_destroy(self, args):
        """destroy: Deletes an instance based on the class name and id
        (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234
        If the class name is missing, print ** class name missing **
        If the class name doesnt exist, print ** class doesn't exist **
        If the id is missing, print ** instance id missing **
        If the instance of the class name doesnt exist for the id,
        print ** no instance found **
        """
        arguments = shlex.split(args)
        if len(arguments) == 0:
            print("** class name missing **")
        elif len(arguments) >= 1 and arguments[0] not in NClass:
            print("** class doesn't exist **")
        elif len(arguments) == 1 and arguments[0] in NClass:
            print("** instance id missing **")
        else:
            flag = 0
            dic = storage.all()
            for key, value in dic.items():
                _id = key.split(".")[1]
                if _id == arguments[1]:
                    flag = 1
                    del dic[key]
                    storage.save()
                    break
            if flag == 0:
                print("** no instance found **")

    def do_all(self, args):
        """all: Prints a list with all string representation of all instances
        based or not on the class name. Ex: $ all BaseModel or $ all
        If the class name doesnt exist, print ** class doesn't exist **
        """
        arguments = shlex.split(args)
        dic = storage.all()
        if len(arguments) == 1 and arguments[0] not in NClass:
            print("** class doesn't exist **")
        elif len(arguments) == 0:
            for key, value in dic.items():
                print(value)
        elif len(arguments) == 1 and arguments[0] in NClass:
            for key, value in dic.items():
                if arguments[0] in key:
                    print(value)

    def do_update(self, args):
        """update:  Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com"
        If the class name is missing, print ** class name missing **
        If the class name doesnt exist, print ** class doesn't exist **
        If the id is missing, print ** instance id missing **
        If the instance of the class name doesnt exist for the id,
        print ** no instance found **
        If the attribute name is missing, print ** attribute name missing **
        If the value for the attribute name doesnt exist,
        print ** value missing **
        """
        arguments = shlex.split(args)
        dic = storage.all()
        if len(arguments) >= 2:
            name = arguments[0] + "." + arguments[1]
        if len(arguments) == 0:
            print("** class name missing **")
        elif len(arguments) > 0 and arguments[0] not in NClass:
            print("** class doesn't exist **")
        elif len(arguments) == 1:
            print("** instance id missing **")
        elif len(arguments) == 2 and name not in dic:
            print("** no instance found **")
        elif len(arguments) == 2:
            print("** attribute name missing **")
        elif len(arguments) == 3:
            print("** value missing **")
        else:
            obj = dic[name]
            setattr(obj, arguments[2], arguments[3])
            obj.save()

    def default(self, args):
        """default function
        """
        arguments = args.split(".")
        if arguments[1] == "all()":
            self.do_all(arguments[0])


if __name__ == "__main__":
    interprete = HBNBCommand()
    interprete.cmdloop()
