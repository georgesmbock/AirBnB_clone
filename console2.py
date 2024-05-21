#!/usr/bin/python3
import cmd
import models
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
        EX: (hbnb) quit
        """
        return True

    def do_EOF(self, line):
        """To exit the program
        EX: (hbnb) EOF or Ctrl + D
        """
        return True

    def emptyline(self):
        """should not execute anything"""
        pass

    def do_create(self, line):
        """Creates a:
           New instance of BaseModel
           Saves it (to the JSON file) and prints id
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

    def do_show(self, line):
        """Prints the string representation of an
           instance based on the class namme and id
           EX: (hbnb) show BaseModel 1234-1234-14234
        """
        lines = line.split()
        if len(lines) == 0:
            print(" ** class missing **")
            return
        if lines[0] not in HBNBCommand.classes:
            print(" ** class doesn't exist ** ")
            return
        if len(lines) < 2:
            print(" ** instance id missing **")
            return
        key = lines[0] + '.' + lines[1]
        all_obj = models.storage.all()
        if key not in all_obj:
            print(" ** instance found **")
            return
        print(all_obj[key])

    def do_destroy(self, line):
        """Deletes an instense based pn the
        class name and id and save the change
        into the JSON file.
        EX:(hbnb) destroy BaseModel 1234-1234-1234
        """
        lines = line.split()
        if len(lines) == 0:
            print(" ** class missing **")
            return
        if lines[0] not in HBNBCommand.classes:
            print(" ** class doesn't exist **")
            return
        if len(lines) < 2:
            print(" ** instance id missing **")
            return
        key = lines[0] + '.' + lines[1]
        all_obj = models.storage.all()
        if key not in all_obj:
            print(" ** no instance found **")
            return
        obj_delete = all_obj[key]
        models.storage.delete(obj_delete)
        models.storage.save()

    def do_all(self, line):
        """Prints all string represntation of
        all instances based oor not on the class
        name.
        EX: (hbnb) all BaseModel
            (hbnb) all
        """
        if not line:
            all_obj = models.storage.all()
        elif line in HBNBCommand.classes:
            all_obj = models.storage.all()
            all_obj[HBNBCommand.classes[line]] = line
        else:
            print(" ** class doesn't exist **")
            return
        instances = [
                    str(obj)
                    for obj in all_obj.values()
                    ]
        print(instances)

    def do_update(self, line):
        """Updates an instance based on the class name and id
        by adding or updating attribute and saves into to
        the JSON file
        EX: (hbnb) update BaseModel 1234-1234-1234 email "aibnb@gmail.com"
        Usage:
            update <class name> <id> <attribute name> "<attribute value>"
        Only one attribute can be updated at the time
        You can assume the attribute name is valid(exists for this model)
        The attribute value must be casted to attribute type
        """
        lines = line.split()
        if len(lines) == 0:
            print(" ** class name mmissing **")
            return
        if lines[0] not in HBNBCommand.classes:
            print(" ** class doesn't exist **")
            return
        if len(lines) < 2:
            print(" ** instance id missing **")
            return
        key = lines[0] + '.' + lines[1]
        all_obj = models.storage.all()
        if key not in all_obj:
            print(" ** no instance found **")
            return
        if len(lines) == 2:
            print(" ** attribute name missing **")
            return
        if len(lines) == 3:
            print(" ** value missing **")
            return
        obj = all_obj[key]
        attr_name = line[2]
        attr_value = line[3]
        if hasattr(obj, attr_name):
            attr_type = type(getattr(obj, attr_name))
            try:
                attr_value = attr_type(attr_value)
            except ValueError:
                print(" ** Value type error **")
                return
        else:
            try:
                attr_value = eval(attr_value)
            except (NameError, SyntaxError):
                pass
        setattr(obj, attr_name, attr_value)
        obj.save()



if __name__ == '__main__':
    HBNBCommand().cmdloop()
