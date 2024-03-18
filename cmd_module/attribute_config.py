#!/usr/bin/python3

"""
Demonstarates attribute configuration in the cmd.Cmd class
These attributes are for controlling command interpreters.
"""

"""
prompt => set to a string that can be printed each
time the user is asked for a new command.

intro => welcome message printed at the start of the program.
Can be set directly on the class
OR cmdloop() takes an argument for this value.

doc_header, misc_header, undoc_header and ruler attributes are used to format help output.
doc_header => header for documented commands
misc_header => header for miscellanous help topics
undoc_header => header for undocumented commands
ruler => default is '='. Character to use under each header
"""
import cmd

class Attributes(cmd.Cmd):
    """
    Simple demo on how to configure attributes.
    """

    prompt = "AirBnB: "
    intro = "Welcome to AirBnB, The Console"

    doc_header = "Documented Commands"
    misc_header = "Misc Commands"
    undoc_header = "Undocumented commands"
    ruler = '-'

    def do_greet(self, line):
        """
        Greets person.
        """
        print("Hello {}".format(line))

    def do_EOF(self, line):
        # Exiting interpreter.
        print("Exiting......")
        return True

    def do_prompt(self, line):
        """
        Changes the prompt.
        """
        self.prompt = line + ':  '


if __name__ == "__main__":
    Attributes().cmdloop()
