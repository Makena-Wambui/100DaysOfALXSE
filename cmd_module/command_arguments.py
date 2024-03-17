#!/usr/bin/python3

"""
This module includes a few enhancements to eliminate some annoyances
and adds help for the greet command.
"""

import cmd


class Hello(cmd.Cmd):
    """
    Class: Hello

    A subclass of Cmd Base Class

    """
    prompt = "Makena$$  "

    def do_greet(self, person):
        """
        Instance Method: do_greet()

        Greets person.
        """
        if person:
            print("Hello, {}".format(person))
        else:
            print("Hello.")

    def do_EOF(self, line):
        """
        Instance Method: do_EOF()

        Cleanly exiting your interpreter.
        """
        return True

    def postloop(self):
        """
        Instance Method: postloop

        A non messy way of exiting the interpreter.
        Adds a new line.
        """
        print()
        

if __name__ == "__main__":
    Hello().cmdloop()
