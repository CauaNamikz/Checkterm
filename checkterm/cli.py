#Import from commands.py and storage.pys
from . import commands, storage, help

#Version number
ver = "Checkterm v0.0.2.2026 / ENG package / ALPHA package"

#Start Text
def run():
    print(ver)
    print("Type 'help' for commands and outputs")
#while Loop for command line
    while True:
        c = input("> ") #Command line input

        if c == "add-entry": 
            commands.add_entry()
        elif c == "add-description":
            commands.add_description()
        elif c == "check-entry":
            commands.check_entry()
        elif c == "complete-entry":
            commands.complete_entry()
        elif c == "uncomplete-entry":
            commands.uncomplete_entry()
        elif c == "remove-entry":
            commands.remove_entry()
        elif c == "list":
            commands.list()
        elif c == "list-incomplete":
            commands.list_incomplete()
        elif c == "list-completed":
            commands.list_completed()
        elif c == "help":
            help.run()
        elif c == "save":
            storage.save()
        elif c == "load":
            storage.load()
        elif c == "quit":
            break
        else:
            print("Invalid command. Type 'help' to see commands.")
