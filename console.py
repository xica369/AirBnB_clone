#!/usr/bin/python3
"""Class HBNBComand that contains the entry point
of the command interpreter
"""
import cmd


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

if __name__ == '__main__':
    interprete = HBNBCommand()
    interprete.cmdloop()
