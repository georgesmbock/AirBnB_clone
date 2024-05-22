#!/usr/bin/python3
"""
    Main console
"""
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """The console"""
    # The prompt is terminal is (hbnb)
    prompt = '(hbnb) '

    classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
            }

    def do_help(self, line):
        """Displays the help according to line argument"""
        super().do_help(line)

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
        print(all_obj[key])

    def do_destroy(self, line):
        """Deletes an instense based pn the
        class name and id and save the change
        into the JSON file.
        EX:(hbnb) destroy BaseModel 1234-1234-1234
        """
        lines = line.split()
        if len(lines) == 0:
            print(" ** class name missing **")
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
        all_obj = models.storage.all()
        if not line:
            print([str(obj) for obj in all_obj.values()])
            return
        elif line in HBNBCommand.classes:
            class_name = line.split()[0]
        else:
            print(" ** class doesn't exist **")
            return
        instances = [
                    str(obj)
                    for obj in all_obj.values()
                    if type(obj).__name__ == class_name
                    ]
        print(instances)

    def do_count(self, line):
        """Retrieves the number of instances of a class"""
        count = 0
        if line:
            lines = line.split()
            if lines[0] in HBNBCommand.classes:
                for key, obj in models.storage.all().items():
                    if key.split('.')[0] == lines[0]:
                        count += 1
            else:
                print(" ** class doesn't exist **")
        else:
            for key, obj in models.storage.all().items():
                count += 1
        print(count)

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
            print(" ** class name missing **")
            return
        class_name = lines[0]
        if class_name not in HBNBCommand.classes:
            print(" ** class doesn't  exist **")
            return
        if len(lines) < 2:
            print(" ** instance id missing **")
            return
        key = lines[0] + '.' + lines[1]
        all_obj = models.storage.all()
        if key not in all_obj:
            print(" ** not instance found **")
            return
        if len(lines) < 3:
            print(" ** attribute name missing **")
            return
        attr_name = lines[2]
        if len(lines) < 4:
            print(" ** value missing **")
        else:
            obj = all_obj[key]
            attr_value = lines[3]
            if hasattr(obj, attr_name):
                obj.save()
            else:
                setattr(obj, attr_name, attr_value.strip('"'))
                obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
