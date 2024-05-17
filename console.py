#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    """The console"""
    prompt = '(hbnb) '

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
