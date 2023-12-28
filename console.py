#!/usr/bin/python3
""" Contains the entry point of the command interpreter """
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """ Entry point of the command interpreter """
    __classes = ["BaseModel"]
    prompt = '(hbnb) '


    def do_create(self, line):
        """
            Creates a new instance of BaseModel, saves it 
            (to the JSON file) and prints the id
            Usage: create <class_name>
        """
        arg = line.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            new_obj = eval(arg[0])()
            print(new_obj.id)
        storage.save()

    
    def do_show(self, line):
        """
            Prints the string representation of an instance based on
            the class name and id
            Usage: show <class_name> <object_id>
        """
        arg = line.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(arg) != 2:
            print("** instance id missing **")
        elif f"{arg[0]}.{arg[1]}" not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()[f"{arg[0]}.{arg[1]}"])

    
    def do_destroy(self, line):
        """
            Deletes an instance based on the class name and id
            (save the change into the JSON file)
            Usage: destroy <class_name> <object_id>
        """
        arg = line.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(arg) != 2:
            print("** instance id missing **")
        elif f"{arg[0]}.{arg[1]}" not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()[f"{arg[0]}.{arg[1]}"]
        storage.save()


    def do_all(self, line):
        """
            Prints all string representation of all instances based or
            not on the class name
            Usage: all <class_name> or all
        """
        arg = line.split()
        if len(arg) == 0:
            print([str(values) for values in storage.all().values()])
        elif arg[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            new_storage = storage.all().items()
            print([str(v) for k, v in new_storage if k.startswith(arg[0])])


    def do_update(self, arg):
        """
            Updates an instance based on the class name and id by
            adding or updating attribute
            Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in storage.all():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            obj_class = args[0]
            obj_id = args[1]
            obj_key = obj_class + "." + obj_id
            obj = storage.all()[obj_key]

            attr_name = args[2]
            attr_value = args[3]

            if attr_value[0] == '"' or attr_value[0] == "'":
                attr_value = attr_value[1:-1]
            
            if hasattr(obj, attr_name):
                type_ = type(getattr(obj, attr_name))
                if type_ in [str, float, int]:
                    attr_value = type_(attr_value)
                    setattr(obj, attr_name, attr_value)
            else:
                setattr(obj, attr_name, attr_value)
            storage.save()



    def do_quit(self, arg):
        """ Quit command to exit the program """
        return True

    def emptyline(self):
        """ Method called when an empty line is
            entered in response to the prompt
        """
        return

    def do_EOF(self, line):
        """ Exits the command interpreter through keyboard interruption """
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()



