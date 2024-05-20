#!/usr/bin/python3
import cmd
from models import storage
from models import BaseModel


class HBNBCommand(cmd.Cmd):
    """This class contains the entry point of
    the command interpreter
    """
    # The prompt is terminal is (hbnb)
    prompt = '(hbnb) '

    classes = {
            "BaseModel": BaseModel
            }

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """To exit the program
        """
        return True

    def emptyline(self):
        """should not execute anything"""
        pass

    def do_create(self, line):
        """Creates a new instances of BaseModel
        EX: (hbnb) create BaseModel
        """
        if not line:
            print(" ** class name missing **")
            return
        elif line not in HBNBCommand.classes:
            print(" ** class doesn't exist **")
            return
        else:
            obj = HBNBCommand.classes[line]()
            obj.save()
            print(obj.id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
