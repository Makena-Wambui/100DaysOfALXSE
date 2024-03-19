This repository contains random concepts i have worked on in my 100DaysOfALXSE Challenge.

DAY ONE
--------
Traps in Bash Scripting
TRAP IN BASH SCRIPTING

Friday, March 15, 2024
9:39 AM

Commands like ls and cd are provided by a third party utility/package, ie the GNU Coreutils Package

But when you create a shell script,  you use keywords like fi, if elif, else, etc.
These are not some binaries living in /usr/bin.
They are commands that are part of the POSIX compliant shell you are using.

In addition to these built-ins like if, for and while, we have the trap built in.

Trap is used to catch or trap supported signals and react upon it.

Run trap -l command to get the list of supported signals.
For ex:
	root@MAKENA:/usr/bin# trap -l
	 1) SIGHUP       2) SIGINT       3) SIGQUIT      4) SIGILL       5) SIGTRAP
	 6) SIGABRT      7) SIGBUS       8) SIGFPE       9) SIGKILL     10) SIGUSR1
	11) SIGSEGV     12) SIGUSR2     13) SIGPIPE     14) SIGALRM     15) SIGTERM
	16) SIGSTKFLT   17) SIGCHLD     18) SIGCONT     19) SIGSTOP     20) SIGTSTP
	21) SIGTTIN     22) SIGTTOU     23) SIGURG      24) SIGXCPU     25) SIGXFSZ
	26) SIGVTALRM   27) SIGPROF     28) SIGWINCH    29) SIGIO       30) SIGPWR
		31) SIGSYS      34) SIGRTMIN    35) SIGRTMIN+1  36) SIGRTMIN+2  37) SIGRTMIN+3
	38) SIGRTMIN+4  39) SIGRTMIN+5  40) SIGRTMIN+6  41) SIGRTMIN+7  42) SIGRTMIN+8
	43) SIGRTMIN+9  44) SIGRTMIN+10 45) SIGRTMIN+11 46) SIGRTMIN+12 47) SIGRTMIN+13
	48) SIGRTMIN+14 49) SIGRTMIN+15 50) SIGRTMAX-14 51) SIGRTMAX-13 52) SIGRTMAX-12
	53) SIGRTMAX-11 54) SIGRTMAX-10 55) SIGRTMAX-9  56) SIGRTMAX-8  57) SIGRTMAX-7
	58) SIGRTMAX-6  59) SIGRTMAX-5  60) SIGRTMAX-4  61) SIGRTMAX-3  62) SIGRTMAX-2
	63) SIGRTMAX-1  64) SIGRTMAX
	
Number before a signal is not a random number or just an index

Instead of using the signal, you can use the number to its right, and you will just as successfully trigger or trap that signal.

For ex if you do kill -9 PID, you are sending the SIGKILL signal to that PID
Recommended to use the signal names themselves because they are easier to read.

When trap built in is used, it listens for signals it supports.
If it is told to check for a signal, when that signal is received by the script, trap executes the action you mentioned.

USAGE AND SYNTAX
	Trap ACTIONS SIGNALS
	
	SIGNALS: one or more signals you want to monitor within the script.
	
	When trap catches even one of the mentioned signals, any ACTIONS you provide will be performed.
	ACTIONS is usually a function call.
	
	1. Best way to use trap is as a clean up of sorts.
	For ex, you are running a task in one of the shell scripts.
	But as the script is running, User presses the Ctrl+C keys.
	How do you clean this up?
	Just use the trap built in
	
	2. You might also want to verify that your script is correctly listening to signals.
	Test by sending a signal externally using the kill command
	We use kill command to send a signal to a process.
	Kill -s <signal> <PID> 
	-s option to specify which signal you want to send
	PID of process to which you want to send the signal.
	
		#!/usr/bin/env bash
		# demonstrate how to use trap for clean up
		
		function signal_interrupt()
		{
		        echo "Sleep interrupted by sig_int."
		}
		function signal_term()
		{
		        echo "Process terminated."
		}
		trap 'signal_interrupt; signal_term; exit' SIGINT SIGTERM
		
		while :
		do
		        echo "Trap listening for interruptions"
		        sleep 2
		done

		
		I ran this script on one terminal.
		Opened another terminal
		Used pgrep to search for the PID of this script
			pgrep -f "trap_demo"
		Sent a SIGTERM signal to that PID using kill command.
			kill -s SIGTERM PID
			
		The script was successfully terminated on the other terminal.


DAY TWO
--------
PASSING ARGUMENTS TO A BASH SHELL SCRIPT AND SPECIAL BASH SHELL VARIABLES
How do you pass variables to shell scripts from the command line?
$0 - name of your bash script
$1 - first bash argument
$2 - second bash argument
$3 - third positional parameter

You can pass multiple arguments to your bash script.

Syntax: script.sh arg1 arg2 ... argn

DAY THREE
-----------
in preparation for the AirBnB Clone, I familiarised myself with the cmd module.


DAY FOUR
---------
Working on My Console

DAY FIVE
--------
Work on AirBnb Clone: the console and models package.

