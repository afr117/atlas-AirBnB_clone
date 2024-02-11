# console.py

import cmd
import models
import os

# Set the file path to the desired location
file_path = os.path.join(current_directory, 'file.json')

# Check if the file exists
if not os.path.exists(file_path):
    print(f"Error: File '{file_path}' not found.")
    # Optionally, you can create the file here if it doesn't exist
    # with open(file_path, 'w') as f:
    #     pass
    # However, ensure that this is the desired behavior

# Attempt to open the file
try:
    with open(file_path, 'r') as file:
        # File operations go here
        pass
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
except Exception as e:
    print(f"Error: {e}")

# Update the file path in models.storage
models.storage._FileStorage__file_path = file_path

# Rest of your code continues here

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

    def do_create(self, arg):
        """
        Create a new instance of BaseModel, save it, and print its id
        """
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Print the string representation of an instance based on class name and id
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            if len(args) < 2:
                print("** instance id missing **")
                return
            instance_id = args[1]
            key = "{}.{}".format(class_name, instance_id)
            all_objs = models.storage.all()
            if key in all_objs:
                print(all_objs[key])
            else:
                print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """
        Delete an instance based on class name and id
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            if len(args) < 2:
                print("** instance id missing **")
                return
            instance_id = args[1]
            key = "{}.{}".format(class_name, instance_id)
            all_objs = models.storage.all()
            if key in all_objs:
                del all_objs[key]
                models.storage.save()
            else:
                print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """
        Print string representations of all instances based or not on class name
        """
        all_objs = models.storage.all()
        if not arg:
            print([str(obj) for obj in all_objs.values()])
            return
        try:
            class_name = arg.split()[0]
            if class_name not in models.storage.classes:
                print("** class doesn't exist **")
                return
            print([str(obj) for key, obj in all_objs.items() if key.split('.')[0] == class_name])
        except IndexError:
            print("** class name missing **")

    def do_update(self, arg):
        """
        Update an instance based on class name and id by adding or updating attribute
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            if class_name not in models.storage.classes:
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            instance_id = args[1]
            key = "{}.{}".format(class_name, instance_id)
            all_objs = models.storage.all()
            if key not in all_objs:
                print("** no instance found **")
                return
            if len(args) < 3:
                print("** attribute name missing **")
                return
            attribute_name = args[2]
            if len(args) < 4:
                print("** value missing **")
                return
            attribute_value = args[3]
            try:
                attribute_value = eval(attribute_value)
            except NameError:
                pass
            setattr(all_objs[key], attribute_name, attribute_value)
            all_objs[key].save()
        except IndexError:
            print("** attribute name missing **")

    def interact_with_console(self):
        """
        Interact with the console commands
        """
        # Instantiate the HBNBCommand class
        console = HBNBCommand()
        console.cmdloop()

if __name__ == '__main__':
    HBNBCommand().cmdloop()

