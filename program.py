"""
    File name: program.py
    Author: Emek Kırarslan
    E-mail: "kirarslanemek@gmail.com"
    Date created: 15/09/2024 - 02:23:32
    Date last modified: 16/09/2024
    Python Version: 3.12.5
    Version: 0.0.1
    License: GNU-GPLv3
    Status: Production
"""    
"""
TODO:
    [X] configuring the program when first started
    [ ] list 
    [ ] create
    [ ] open
"""
from helper_functions import *
from pyfiglet import Figlet
from rich import print
from rich.rule import Rule
from rich.console import Console
from rich.table import Table
from rich.text import Text
from rich import box

import configparser, random, requests
from time import sleep
import os
import cmd
import sys

class Not(cmd.Cmd):
    console = None
    prompt = "> "
    ruler = u'─'

    home_dir = ""
    notebook_directory = ""
    config_file = ""

    testsettingvar = ""
    
    notebooks = {
        "unorganized": [f"note_{i}.txt" for i in range(10)],
        "work": [f"work_note_{i}.txt" for i in range(5)],
        "personal": [f"personal_note_{i}.txt" for i in range(3)]
    }
    def preloop(self):
         """Initialization before the command loop starts."""
         self.console = Console()
         self.intro_text()
         self.check_configuration()
         self.read_configuration()

    def check_configuration(self):
        """This will check if configuration is setup correctly."""
        self.home_dir = os.path.expanduser("~")
        self.notebook_directory = os.path.join(self.home_dir, ".n/notebooks")
        self.config_file = os.path.join(self.home_dir, ".n/config.ini")
        if(os.path.isdir(self.notebook_directory) and os.path.isfile(self.config_file)):
            return True
        else:
            print("[bold red]not. is not configured correctly.[/bold red]")
            i = input("Do you want to automatically configure? (y/n)")
            if(i == "y"):
                with self.console.status("[bold green]Creating files...") as status:                
                    os.makedirs(self.notebook_directory, exist_ok=True)
                    open(self.config_file, 'w').close()
                    sleep(1)
                    self.console.print("[bold green]Configured![/bold green]")
            else:
                print("Exiting...")
                exit()
    def read_configuration(self):
        configfile = configparser.ConfigParser()
        configfile.read(self.config_file)
        self.testsettingvar = configfile.get('Settings', 'testsettingvar', fallback="test")
        
    
        
    def do_settings(self, arg):
        """Print the setting values."""
        print("")
        self.console.rule("not. Settings")
        #print("not. Settings")
        #print(u'─'*os.get_terminal_size().columns)
        #self.console.print(Text("Current Settings"), justify="center")
        self.console.print()
        #self.console.print(Rule("Current Settings"), width=os.get_terminal_size().columns)
        print("Notebook Directory = ", self.notebook_directory)
        print("Config file = ", self.config_file)
        print("Current theme = default" )
        print("")
        print("To configure settings, please type [underline yellow]set[/underline yellow]")
       
    def do_test(self, arg):
        """Testing stuff"""
        print(self.testsettingvar)
            
    def do_set(self, arg):
        """Set config values."""
        if(arg == "notebook-dir"):
                    print("Please enter a valid [magenta]heldirectory.[/magenta]")
        else:
            print_set_help()

    def do_create(self, arg):
        """Create notes, notebooks etc."""
        args = arg.split()
        if not args:
            print_create_help()
            return
        if args[0] == "note":
            if(len(args) == 1):
                #No argument is given.
                print("Editor will open...")
            elif(len(args) == 2):
                note_body = args[1]
                print(f"A note with {note_body} inside is created")
            elif(len(args) == 3):
                note_name = args[1]
                note_body = args[2]
                print(f"The note {note_name} with {note_body} inside is created")
            else:
                print_create_help()
        elif args[0] == "notebook":
            if(len(args) == 1):
                print("Please specify a name: ")
                i = input("")
            if(len(args) == 2):
                notebook_name = args[1]
                print("Notebook named {notebook_name} is created")
            else:
                print_create_help()
        else:
            print_create_help()     
          
    def do_list(self, arg):
        """List notes and notebooks"""
        args = arg.split()
        if not args:
            print_list_help()
            return

        if args[0] == "notes":
            if len(args) == 1:
                print("")
                grid = Table(expand=True, highlight=True, box=None)
                grid.add_column(f"Notes from the [yellow]unorganized[/yellowq] notebook")
                for idx, note in enumerate(self.notebooks["unorganized"]):
                    grid.add_row(f"[bold]{idx}[/bold] - {note}")
                print(grid)
                print("")
            elif len(args) == 2:
                notebook = args[1]
                if notebook in self.notebooks:
                    print("")
                    grid = Table(expand=True, highlight=True, box=None)
                    grid.add_column(f"Notes from the [magenta]{notebook}[/magenta] notebook")
                    for idx, note in enumerate(self.notebooks[notebook]):
                        grid.add_row(f"[bold]{idx}[/bold] - {note}")
                    print(grid)
                    print("")
                else:
                    print("")
                    print(f"There is no notebook named [bold]{notebook}[/bold].")
                    print("")
        elif args[0] == "notebooks":
            print("")
            grid = Table(expand=True, highlight=True, box=None)
            grid.add_column("Available notebooks")
    
            for notebook in self.notebooks:
                #print(f"  - {notebook}")
                grid.add_row(f"{notebook}", "")
            print(grid)
            print("")

        else:
            print_list_help()
        
                
    

    #------------MISC--------------
    def do_helpa(self, arg):
        """Show help for the commands."""
        print_general_help(self, arg)
    def do_quit(self, arg):
        """Quit the application."""
        print("[bold]Quitting...[/bold]")
        print("[bold]Take care :)[/bold]")
        return True
    def do_q(self, arg):
        """Quit the application."""
        print("[bold]Quitting...[/bold]")
        print("[bold]Take care :)[/bold]")
        return True
    def do_exit(self, arg):
        """Exit the application."""
        print("[bold]Exiting...[/bold]")
        print("[bold]Take care :)[/bold]")
        return True
    def do_clear(self, arg):
        """Clear the screen."""
        os.system('cls' if os.name == 'nt' else 'clear')
        self.intro_text()             
    def default(self, line):
        """Called when the command is not recognized."""
        print(f"Unknown command: {line}")
    def intro_text(self):
        custom_fig = Figlet(font='smslant')
        fig_text = custom_fig.renderText('not.')
        print(f"[magenta]{fig_text}[/magenta]")
        print("[bold magenta]not.[/bold magenta] is a simple note-taking CLI application written in [bold green]Python.[/bold green]")
        print("To see available commands, please type [bold underline yellow]help[/bold underline yellow].")


if __name__ == '__main__':
    Not().cmdloop()
        
