#!/usr/bin/python3
"""
How to override base class methods.
"""
import cmd


class Illustrate(cmd.Cmd):
    """
    Illustrates base class method use.
    """
    def cmdloop(self, intro=None):
        """
        Main processing loop of the Interpreter.
        Can be overriden but it is usually unnecessary.
        Since preloop() and postloop() hooks are available.
        """
        print("cmdloop({})".format(intro))
        return cmd.Cmd.cmdloop(self, intro)

    def preloop(self):
        """
        Hook method excecuted once when cmdloop() is called.
        Prints preloop.
        """
        print("preloop()")

    def postloop(self):
        """
        Hook method exceuted once when cmdloop() is abt to return.
        Prints postloop()
        """
        print("postloop()")

    def parseline(self, line):
        """
        Actual input line is parsed with parseline()
        Creates a tuple containing the command, and
        the remaining portion of the line.
        """
        print("parseline({}) => ".format(line))
        ret = cmd.Cmd.parseline(self, line)
        print("{}".format(ret))
        return ret

    def onecmd(self, s):
        """
        Each iteration thro the cmdloop call onecmd to dispatch the command
        to its appropriate processor.
        """
        print("onecmd({})".format(s))
        return cmd.Cmd.onecmd(self, s)

    def emptyline(self):
        """
        If an empty line is entered, emptyline is called.
        bY default, it reruns the last nonempty command entered.
        """
        print("emptyline()")
        print('\n')
        # return cmd.Cmd.emptyline(self)

    def default(self, line):
        """
        If the command prefix is not recognized, default() is called.
        By default, it prints an error message then returns.
        """
        print("default({})".format(line))
        return cmd.Cmd.default(self, line)

    def precmd(self, line):
        """
        Executed before the input line is interpreted, but after the prompt
        is generated and issued.
        If the input line is not empty, precmd() is called.
        Then that command's processor is looked up and invoked.
        If there is no processor for that command, then default is called.
        """
        print("precmd({})".format(line))
        return cmd.Cmd.precmd(self, line)

    def postcmd(self, stop, line):
        """
        Hook method that is executed after a command dispatch is completed.
        Line -> command line which was executed.
        Stop is a flag which indicates whether the exceution will be terminated
        after call to postcmd().
        This will be the return value of onecmd().
        """
        print("postcmd({})".format(line))
        return cmd.Cmd.postcmd(self, stop, line)

    def do_greet(self, line):
        """
        Greets person.
        """
        print("Hello, {}.".format(line))

    def do_EOF(self, line):
        """
        Clean way of exiting interpreter.
        """
        print("Exiting..")
        return True


if __name__ == "__main__":
    Illustrate().cmdloop('Illustrating methods of cmd.Cmd')
