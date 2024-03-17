#!/usr/bin/python3
"""
Implementing a help handler for the greet command
"""

import cmd


class Hello(cmd.Cmd):
    """
    class: Hello

    A subclass of the Cmd base class.
    """

    prompt = "Makena$$  "

    def do_greet(self, person):
        """
        Instance method. do_greet()

        Command handler for the greet command.

        Greets the named person.
        """
        if person:
            print("Hello, {}".format(person))
        else:
            print("Hello.")

    def help_greet(self):
        """
        When present, help handler is called to produce
        help text for the named command.
        """
        print('\n'.join(['Greet [person]', 'Greets the named person']))

    def do_EOF(self, line):
        """
        Instance method: do_EOF()

        Provides a clean way of exiting the interpreter.
        """
        return True

    def postloop(self):
        """
        Instance method: postloop

        Prints a new line hence providing a non messy way of exiting.
        """
        print()


if __name__ == "__main__":
    Hello().cmdloop()
