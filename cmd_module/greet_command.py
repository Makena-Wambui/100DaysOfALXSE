#!/usr/bin/python3

"""
A simple program that supports the greet command.
Building a simple command processor using the cmd module.
"""

import cmd


class Hello(cmd.Cmd):
    """
    Class: Hello

    A subclass of Cmd Base Class.
    """

    def do_greet(self, line):
        """
        Instance Method: do_greet

        Supports the greet command.
        """
        print("Hello!")

    def do_EOF(self, line):
        """
        Instance method: do_EOF()

        Implement do_EOF() and have it return true to have a clean way
        of exiting your interpreter.
        """
        print()
        return True



if __name__ == "__main__":
    hey = Hello()
    hey.prompt = "Makena$  "
    hey.cmdloop()
