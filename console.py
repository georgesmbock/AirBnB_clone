#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import models


class HBNBCommand(cmd.Cmd):
    """The Main console"""
    """ The prompt of teh console"""
    prompt = '(hbnb) '

    classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
           }

    def do_help(self, line):
        """"Displays the help according to line argument"""
        super().do_help(line)

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_create(self, line):
        """Creates a:
           new instance of BaseModel
           Saves it (to the JSON file) and
           prints the id
           EX $ create BaseModel
        """
        if not line:
            print("** class name missing **")
            return
        if line not in HBNBCommand.classes:
            print("** class doesn't eixtts **")
            return
        obj = HBNBCommand.classes[line]()
        obj.save()
        print(obj.id)

    def do_show(self, lines):
        """Prints the string representation
        of an instance based on the class name
        and id
        Ex: $ show BaseModel 1234-1234-1234"""
        line = lines.split()
        if len(line) == 0:
            print("** class name missing **")
            return
        if line[0] not in HBNBCommand.classes:
            print("** class doesn't exists **")
            return
        if len(line) < 2:
            print("** instance id missing **")
            return
        key = line[0] + '.' + line[1]
        all_obj = models.storage.all()
        if key not in all_obj:
            print("** no instance found **")
            return
        print(all_obj[key])

    def do_destroy(self, lines):
        """Deletes an instance based on the
        class name and id and saves the change
        into the JSON file.
        EX: $ destroy BaseModel 1234-1234-1234
        """
        line = lines.split()
        if len(line) == 0:
            print("** class name missing **")
            return
        if line[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(line) < 2:
            print("** instance id missing **")
            return
        key = line[0] + '.' + line[1]
        all_obj = models.storage.all()
        if key not in all_obj:
            print("** no instance found **")
            return
        obj_delete = all_obj[key]
        models.storage.delete(obj_delete)
        models.storage.save()

    def do_all(self, lines):
        """Prints all string representation of
        all instances based or not on the class
        name.
        EX: $ all BaseModel
            $ all
        """
        # line = lines.split()if len(line) == 0:
        if not lines:
            all_obj = models.storage.all()
        elif lines in HBNBCommand.classes:
            all_obj = models.storage.all(HBNBCommand.classes[lines])
        # print([str(obj) for obj in all_obj.values()])
        else:
            # if line[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        # all_obj = models.storage.all() class_name = line[0]
        instances = [
                    str(obj)
                    for obj in all_obj.values()
                    ]
        # if type(obj).__name__ == class_name
        print(instances)

    def do_update(self, lines):
        """Updates an instances based on the class name and id by
        adding or updating attribute and saves into to the JSON file
        EX: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        Usage:
            update <class name> <id> <attribute name> "<attribute value>"
        Only one attribute can be updated at the time
        You can assume the attribute name is valid(exists for this model)
        The attribute value must be casted to attribute type
        """
        line = lines.split()
        if len(line) == 0:
            print("** class name missing **")
            return
        if line[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(line) < 2:
            print("** instance id missing **")
            return
        key = line[0] + "." + line[1]
        all_obj = models.storage.all()
        if key not in all_obj:
            print("** no instance found **")
            return
        if len(line) < 3:
            print("** attribute name miising **")
            return
        if len(line) < 4:
            print("** value missing **")
            return
        obj = all_obj[key]
        attr_name = line[2]
        attr_value = line[3]
        if hasattr(obj, attr_name):
            attr_type = type(getattr(obj, attr_name))
            try:
                attr_value = attr_type(attr_value)
            except ValueError:
                print("** Value type error **")
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
