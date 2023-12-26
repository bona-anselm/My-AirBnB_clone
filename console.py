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
        """
        arg = line.split()
        if len(arg) == 0:
            print('** class name missing **')
        elif arg[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            new_obj = eval(arg[0])()
            print(new_obj.id)
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



