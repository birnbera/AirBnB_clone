#!/usr/bin/python3
"""Python console prints prompt and quits"""


import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """End of file - quits console"""
        return True

    def do_quit(self, line):
        """quits console"""
        return True

if __name__ == '__main__':
    """command loop"""
    HBNBCommand().cmdloop()
