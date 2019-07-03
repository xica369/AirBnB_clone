#!/usr/bin/python3
"""Class HBNBComand that contains the entry point
of the command interpreter
"""
import cmd
from models import base_model
from models.engine import file_storage


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

    def do_create(self, args):
        """create: Creates a new instance of BaseModel,
        saves it (to the JSON file)
        and prints the id. Ex: $ create BaseModel
        If the class name is missing, print ** class name missing **
        If the class name doesnt exist, print ** class doesn't exist **
        """
        arguments = args.split()
        if len(arguments) == 0:
            print("** class name missing **")
        elif len(arguments) == 2 and arguments[1] == "BaseModel":
            new_base_model = BaseModel()
            FileStorage.new(new_base_model)
            FileStorage.save()
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
        arguments = args.split()
        if len(argments) == 0:
            print("** class name missing **")
        else:
            if arguments[0] is not "BaseModel":
                print("** class doesn't exist **")
            if len(arguments) < 2:
                print("** instance id missing **")
            flag = 0
            for key, value in FileStorage.__objects.items():
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
        arguments = args.split()
        if len(arguments) == 0:
            print("** class name missing **")
        else:
            if arguments[0] is not "BaseModel":
                print("** class doesn't exist **")
            if len(arguments) < 2:
                print("** instance id missing **")
            if len(arguments) == 2:
                flag = 0
                for key, value in FileStorage.__objects.items():
                    _id = key.split(".")[1]
                    if _id == arguments[1]:
                        flag = 1
                        del FileStorage.__objects[key]
                        FileStorage.save()
                        break
                if flag == 0:
                    print("** no instance found **")

    def do_all(self, args):
        """all: Prints a list with all string representation of all instances
        based or not on the class name. Ex: $ all BaseModel or $ all
        If the class name doesnt exist, print ** class doesn't exist **
        """
        arguments = args.split()
        if len(arguments) == 1 and arguments[0] is not "BaseModel":
            print("** class doesn't exist **")
        if len(arguments) > 1:
            pass
        else:
            for key, value in FileStorage.__objects.items():
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
        arguments = args.split()
        flag = 0
        if len(arguments == 0):
            print("** class name missing **")
        if len(arguments) > 0 and arguments[0] is not "BaseModel":
            prints("** class doesn't exist **")
            flag1 = 1
        if len(arguments == 1):
            print("** instance id missing **")
        flag1 = 0
        for key, value in FileStorage.__objects.items():
            _id = key.split(".")[1]
            if _id == arguments[1]:
                flag = 1
                break
        if flag == 0:
            print("** no instance found **")
        if len(arguments) == 2:
            print("** attribute name missing **")
        flag2 = 0
        #verificar que el attribute name es existe, si existe flag2 = 1
        if len(arguments) == 3:
            print("** value missing **")
        if len(arguments) > 3 and flag == 0 and flag1 == 1 and flag2 == 1:
            #actualizar datos


if __name__ == "__main__":
    interprete = HBNBCommand()
    interprete.cmdloop()
