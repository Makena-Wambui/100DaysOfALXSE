#!/usr/bin/python3
"""
Demonstrate argument completion using the "complete_" methods.
"""

import cmd

class Hello(cmd.Cmd):
    """
    Class: Hello.

    A subclass of Base Class Cmd.
    """
    prompt = "Makena$$  "

    FREINDS = ["Alice", "August", "Cindy", "David", "Gene", "Zeke", "Jake"]
    # FRIENDS receive a less formal greeting compared to named or anynomous persons.

    def do_greet(self, person):
        """
        Greets the named person.
        """
        if person and person in self.FREINDS:
            greeting = f"Hello, {person}! Whatsup."

        elif person:
            greeting = f"Hello, {person}."

        else:
            greeting = "Hello."

        print(f"{greeting}")

    def complete_greet(self, text, line, begidx, endix):
        """
        When user provides input text, this method returns a list of 
        friends that match.
        Otherwise, if no input text, the whole list of friends is returned.
        """
        if not text:
            completions = self.FREINDS[:]

        else:
            completions = [name for name in self.FREINDS if name.startswith(text)]

        return completions

    def do_EOF(self, line):
        """
        Cleanly exiting your interpreter
        """
        return True
        

    def postloop(self):
        """
        Prints a new line for a more presentable interface.
        """
        print()


if __name__ == "__main__":
    Hello().cmdloop()
