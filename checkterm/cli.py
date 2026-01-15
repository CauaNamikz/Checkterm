#Import from commands.py and storage.pys
from . import commands, storage, help

#Version number
ver = "Checkterm v0.5.0.2026 / ENG package / BETA package"

#Start Text
def run():
    print("Do you want to load a file? (Y/N)")
    fileload = input("> ")
    if fileload == "Y":
        storage.load()
    elif fileload == "N":
        print()
    else:
        print("Invalid command. Type Y for yes and N for no. Your file will not be loaded unless you use the load command.")
    print(ver)
    print("Type 'help' for commands and outputs")
#while Loop for command line
    while True:
        c = input("> ") #Command line input

        if c == "add-checklist":
            commands.add_checklist()
        
        elif c == "add-entry": 
            commands.add_entry()

        elif c == "edit-checklist-description":
            commands.edit_checklist_description()
        
        elif c == "edit-entry-description":
            commands.edit_entry_description()

        elif c == "check-checklist":
            commands.check_checklist()
        
        elif c == "check-entry":
            commands.check_entry()
       
        elif c == "edit-checklist-name":
            commands.edit_checklist_name()
        
        elif c == "edit-entry-name":
            commands.edit_entry_name()
        
        elif c == "complete-entry":
            commands.complete_entry()
        
        elif c == "uncomplete-entry":
            commands.uncomplete_entry()
        
        elif c == "remove-entry":
            commands.remove_entry()
        
        elif c == "list":
            commands.list()
        
        elif c == "list-checklists":
            commands.list_checklists()

        elif c == "list-checklist-entries":
            commands.list_checklist_entries()
        
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
