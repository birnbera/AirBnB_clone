#!/usr/bin/python3
"""Python console prints prompt and quits"""

from datetime import datetime
import cmd
import re
import models


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """
        EOF:
        End of file. Exits the console.
        """
        return True

    def do_quit(self, line):
        """
        quit:
        Exits the console.
        """
        return True

    def emptyline(self):
        pass

    def do_create(self, line):
        """
        create:

        Creates a new instance of BaseModel, saves it and prints the id.

        This method breaks a string of arguments down into smaller chunks,
        or strings. It will try to return the value of the named attribute.
        That will be stored, saved, and printed. If the named attribute
        doesn't exist, AttributeError is raised and "** class doesn't exist **"
        will be printed to the screen.

        If the class name is missing, "** class name missing **" will be
        printed to the screen.
        """
        if len(line) == 0:
            print("** class name missing **")
        else:
            args = line.split()
            try:
                cls = getattr(models, args[0])
            except AttributeError:
                print("** class doesn't exist **")
                return
            obj = cls()
            obj.save()
            print(obj.id)

    def do_show(self, line):
        """
        show:

        Prints the string representation of an instance - class name and id

        This method splits the arguments into smaller strings before the
        arguments are used. If the length of the arguments is less than two,
        "** instance id missing **" will print to the screen since more than
        one argument is needed. However, if an appropriate amount of arguments
        is available, the result of class name and id will print to the screen.
        Otherwise, KeyError will be raised and "** no instance found **" will
        be printed to the screen.

        If the class name is missing, "** class name missing **" will be
        printed to the screen. If the class name doesn't exist, "** class
        doesn't exist **" will be printed to the screen. 
        """
        if len(line) == 0:
            print("** class name missing **")
        else:
            args = line.split()
            if hasattr(models, args[0]):
                if len(args) < 2:
                    print("** instance id missing **")
                else:
                    obj_id = '.'.join(args[:2])
                    try:
                        print(models.storage.all()[obj_id])
                    except KeyError:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_destroy(self, line):
        """
        destroy:

        Deletes an instance based on the class name and id.

        In order for the destroy method to work, it will need two arguments. The
        arguments will be broken

        If the class name is missing, "** class name missing **" will be printed to
        the screen. If class name doesn't exist, "** class doesn't exist **" will
        be printed to the screen.
        """
        if len(line) == 0:
            print("** class name missing **")
        else:
            args = line.split()
            if hasattr(models, args[0]):
                if len(args) < 2:
                    print("** instance id missing **")
                else:
                    obj_id = '.'.join(args[:2])
                    try:
                        del models.storage.all()[obj_id]
                        models.storage.save()
                    except KeyError:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_all(self, line):
        if len(line) > 0:
            line = line.split()[0]
        list_found = []
        if line == "" or hasattr(models, line):
            for k, v in models.storage.all().items():
                if line in k:
                    list_found.append(str(v))
            print(list_found)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        pattern = "[^\s\"\']+|\"[^\"]*\"|\'[^\']*\'"
        pattern = re.compile(pattern)
        if len(line) == 0:
            print("** class name missing **")
        else:
            args = re.findall(pattern, line)
            for i, arg in enumerate(args):
                args[i] = arg.strip("\"'")
            if not hasattr(models, args[0]):
                print("** class doesn't exist **")
                print(args)
                return
            try:
                obj_id = '.'.join([args[0], args[1]])
            except IndexError:
                print("** instance id missing **")
                return
            try:
                obj = models.storage.all()[obj_id]
            except KeyError:
                print("** no instance found **")
                return
            try:
                attr = args[2]
            except IndexError:
                print("** attribute name missing **")
                return
            try:
                val = args[3]
            except IndexError:
                print("** value missing **")
                return
            setattr(obj, attr, val)
            obj.save()

if __name__ == '__main__':
    """command loop"""
    HBNBCommand().cmdloop()
