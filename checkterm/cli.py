from . import commands, storage

ver = "Checkterm v0.0.1.2026 / ENG package / ALPHA package"

def run():
    print(ver)
    print("Type 'help' for commands and outputs")

    while True:
        commandline = input("> ")

        if commandline == "add-entry":
            commands.add_entry()
        elif commandline == "complete-entry":
            commands.complete_entry()
        elif commandline == "remove-entry":
            commands.remove_entry()
        elif commandline == "list-active":
            commands.list_active()
        elif commandline == "list-state-0":
            commands.list_state_0()
        elif commandline == "list-state-1":
            commands.list_state_1()
        elif commandline == "help":
            commands.help_command()
        elif commandline == "save":
            storage.save()
        elif commandline == "load":
            storage.load()
        elif commandline == "quit":
            break
        else:
            print("Invalid command. Type 'help' to see commands.")
