#!/usr/bin/python3
"""
This module defines the HBNBCommand class.
"""
import cmd

class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class for the command interpreter.
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program
        """
        print()  # Print a newline for better formatting
        return True

    def emptyline(self):
        """
        Do nothing on empty input line
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

