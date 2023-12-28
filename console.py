#!/usr/bin/python3
""" Contains the entry point of the command interpreter """
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """ Entry point of the command interpreter """
    __classes = ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]
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


    def default(self, arg):
        """ Update your command interpreter to retrieve all
            instances of a class
                Usage: <class name>.all()
            Update your command interpreter to retrieve
            the number of instances of a class
                Usage: <class name>.count()
            Update your command interpreter to retrieve
            an instance based on its ID
                Usage: <class name>.show(<id>)
            Update your command interpreter to destroy an
            instance based on his ID
                Usage: <class name>.destroy(<id>)
            Update your command interpreter to update an
            instance based on his ID
            Usage: <class name>.update(<id>, <attr name>, <attr value>)
            Update your command interpreter to update an
            instance based on his ID with a dictionary
            Usage: <class name>.update(<id>, <dictionary representation>)
        """
        args = arg.split('.')
        if args[0] in self.__classes:
            if args[1] == 'all()':
                self.do_all(args[0])
            elif args[1] == 'count()':
                list_count = [v for k, v in storage.all().items() if k.startswith(args[0])]
                print(len(list_count))
            elif args[1].startswith('show'):
                id_ = args[1].split('"')[1]
                self.do_show(f"{args[0]} {id_}")
            elif args[1].startswith('destroy'):
                id_ = args[1].split('"')[1]
                self.do_destroy(f"{args[0]} {id_}")
            elif args[1].startswith('update'):
                split_ = args[1].split('(')
                split_ = split_[1].split(')')
                split_ = split_[0].split(', ')

                id_ = split_[0].strip('"')
                attr_name = split_[1].strip('"')
                attr_value = split_[2].strip('"')
                self.do_update(f"{args[0]} {id_} {attr_name} {attr_value}")


if __name__ == '__main__':
    HBNBCommand().cmdloop()



