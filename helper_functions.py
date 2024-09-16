from rich import print
from rich.rule import Rule
from rich.console import Console
from rich.table import Table
from rich.text import Text
from rich import box

def print_set_help():
    print("")
    grid = Table(expand=True, highlight=True, box=None)
    grid.add_column("Available commands")
    grid.add_column("Description", justify="left")
    grid.add_row("set notebook-dir <directory>", "[italic]Sets the notebook directory (default=~/.not/Notebooks)[/italic]")
    grid.add_row("set config-dir <directory>", "[italic]Sets the config directory (default=~/.config/not/config.ini)[/italic]")
    grid.add_row("set theme <string>", "[italic]Sets the theme[/italic]")
    print(grid)
    print("")

def print_create_help():
    print("")
    grid = Table(expand=True, highlight=True, box=None)
    grid.add_column("Available commands")
    grid.add_column("Description", justify="left")
    grid.add_row("create note", "[italic]Open the note editor[/italic]")
    grid.add_row("create note <content>", "[italic]Create a note with <content> as a content.[/italic]")
    grid.add_row("create note <file_name> <content>", "[italic]Create a note named <file_name> with <content> as a content.[/italic]")
    grid.add_row("create notebook <name>", "[italic]Create a notebook named <name>.[/italic]")
    print(grid)
    print("")

def print_list_help():
    print("")
    grid = Table(expand=True, highlight=True, box=None)
    grid.add_column("Available commands")
    grid.add_column("Description", justify="left")
    grid.add_row("list notes", "[italic]Print notes from the unorganized folder[/italic]")
    grid.add_row("list notes <notebook>", "[italic]Print notes from a specific notebook[/italic]")
    grid.add_row("list notebooks", "[italic]Print all notebooks[/italic]")
    print(grid)
    print("")


def print_general_help(main, arg):
    if arg == "test":
        print("[reverse]is it?[/reverse]")
    else:
        
        print("")
        main.console.rule("not. Help")
        print("")
        print("USAGE:")
        print("     [OPTIONS] <SUBCOMMANDS>")
        print("OPTIONS:")
        print("     add <string> - add note to current notebook")
        print("     list - list notes in the current notebook")
        print("     notebook - get information about current notebook")
        print("SUBCOMMANDS:")
        print("     add:")
        print("         ")
