#!/usr/bin/python3
"""Defines the HBNBCommand class"""

import cmd


class HBNBCommand(cmd.Cmd):
    """HBNBCommand commands"""

    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit the console"""
        return True

    def do_EOF(self, line):
        """Exit the console"""
        return True

    def emptyline(self):
        """an empty line + ENTER shouldn’t execute anything"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
