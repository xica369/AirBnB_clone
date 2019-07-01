#!/usr/bin/python3
"""Class HBNBComand that contains the entry point
of the command interpreter
"""
import cmd
from models.base_model import BaseModel


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

    def get_arguments(args):
        """divides the string and get the arguments
        """
        arguments = args.split()
        return arguments

    def do_create(self, args):
        """create: Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id. Ex: $ create BaseModel
        If the class name is missing, print ** class name missing **
        If the class name doesnt exist, print ** class doesn't exist **
        """
        arguments = get_arguments(args)
        if len(arguments) < 2:
            print("** class name missing **")
        if len(arguments) == 2 and arguments[1] == "BaseModel":
            new_base_model = BaseModel()
            # saves it (to the JSON file)
            print("{}".format(new_base_model.id))

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
        arguments = get_arguments(args)
        if len(argments) == 0:
            print("** class name missing **")
        else:
            if arguments[0] is not "BaseModel":
                print("** class doesn't exist **")
            if len(arguments) < 2:
                print("** instance id missing **")
            #If the instance of the class name doesnt exist for the id

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
        arguments = get_arguments(args)
        if len(arguments) == 0:
            print("** class name missing **")
        else:
            if arguments[0] is not "BaseModel":
                print("** class doesn't exist **")
            if len(arguments) < 2:
                print("** instance id missing **")
            #If the instance of the class name doesnt exist for the id

    def do_all(self, args):
        """all: Prints a list with all string representation of all instances
        based or not on the class name. Ex: $ all BaseModel or $ all
        If the class name doesnt exist, print ** class doesn't exist **
        """
        arguments = get_arguments(args)
        if arguments[0] is not "BaseModel":
            print("** class doesn't exist **")
        #

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
        #

if __name__ == '__main__':
    interprete = HBNBCommand()
    interprete.cmdloop()
