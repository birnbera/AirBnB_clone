#!/usr/bin/python3
"""Python console prints prompt and quits"""

from datetime import datetime
import cmd
import re
import models

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """End of file - quits console"""
        return True

    def do_quit(self, line):
        """quits console"""
        return True

    def emptyline(self):
        pass

    def do_create(self, line):
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
            if attr in ['created_at', 'updated_at']:
                try:
                    val = datetime.strptime(val, '%Y-%m-%dT%H:%M:%S.%f')
                except:
                    print("cannot set datetime with: {}".format(val))
                    return
            setattr(obj, attr, val)
            obj.save()

if __name__ == '__main__':
    """command loop"""
    HBNBCommand().cmdloop()
