#!/usr/bin/python3
"""Defines the HBNB console."""
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage

class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter."""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print()
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel/User, saves it (to the JSON file) and prints the id."""
        if not arg:
            print("** class name missing **")
            return
        try:
            if arg == "BaseModel":
                obj = BaseModel()
            elif arg == "User":
                obj = User()
            else:
                print("** class doesn't exist **")
                return
            obj.save()
            print(obj.id)
        except Exception as e:
            print(e)

    def do_show(self, arg):
        """Print the string representation of an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        try:
            print(storage.all()[key])
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        try:
            del storage.all()[key]
            storage.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, arg):
        """Print all string representation of all instances based or not on the class name."""
        if arg:
            if arg not in ["BaseModel", "User"]:
                print("** class doesn't exist **")
                return
            objs = [str(obj) for key, obj in storage.all().items() if arg in key]
        else:
            objs = [str(obj) for obj in storage.all().values()]
        print(objs)

    def do_update(self, arg):
        """Update an instance based on the class name and id by adding or updating attribute."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        obj = storage.all()[key]
        setattr(obj, args[2], args[3])
        obj.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
