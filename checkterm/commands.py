#Base of commands for CLI

#Import from state.py
from . import state


#Output
OUTPUT_END = "Task finished with output"
OUTPUT_SUCCESS = 0
OUTPUT_INVALID = 1


# Help texts
#Commands
ADD_ENTRY_HELP = "add-entry - Add entries "
COMPLETE_ENTRY_HELP = "complete-entry - Complete entries"
REMOVE_ENTRY_HELP = "remove-entry - Remove entries"
SAVE_HELP = "save - Save checklist"
LOAD_HELP = "load - Load checklist"
LIST_HELP = "list - List entries"
LIST_INCOMPLETE_HELP = "list-incomplete - List incomplete entries"
LIST_COMPLETED_HELP = "list-completed - List completed entries"
QUIT_HELP = "quit - Quit the program"
#Outputs
OUTPUT_0_HELP = "0 - Sucess"
OUTPUT_1_HELP = "1 - Error (invalid)"


# Commands
def list():
    print("Entradas atuais:")
    for entry in state.entries:
        print("ID", entry["id"], "-", entry["name"])

def add_entry(): #Add entry
    name = input("Entry name > ")

    if name.strip() == "":
        print(OUTPUT_END, OUTPUT_INVALID)
        return

    state.entries.append({
        "id": state.get_next_id(),
        "name": name,
        "completed": 0
    })

    print(OUTPUT_END, OUTPUT_SUCCESS)


def complete_entry(): #Complete entry
    list()
    id_ = int(input("ID for next completed entry > "))

    for entry in state.entries:
        if entry["id"] == id_:
            entry["completed"] = 1
            print(OUTPUT_END, OUTPUT_SUCCESS)
            return
        else:
            print(OUTPUT_END, OUTPUT_INVALID)


def remove_entry(): #Remove entry
    list()
    id_ = int(input("ID for next removed entry > "))

    for entry in state.entries:
        if entry["id"] == id_:
            state.entries.remove
            print(OUTPUT_END, OUTPUT_SUCCESS)
            return
        else:
            print(OUTPUT_END, OUTPUT_INVALID)


def list_incomplete(): #List incomplete entries
    print("Incomplete entries:")
    for entry in state.entries:
        if entry["completed"] == 0:
            print("ID", entry["id"], "-", entry["name"])
        else:
            print("No entries incomplete.")


def list_completed(): #List complete entries
    print("Complete entries:")
    for entry in state.entries:
        if entry["completed"] == 1:
            print("ID", entry["id"], "-", entry["name"])
        else:
            print("No entries completed.")


def help_command(): #Help
    print("Command list:")
    print(ADD_ENTRY_HELP)
    print(COMPLETE_ENTRY_HELP)
    print(REMOVE_ENTRY_HELP)
    print(LIST_HELP)
    print(LIST_INCOMPLETE_HELP)
    print(LIST_COMPLETED_HELP)
    print(SAVE_HELP)
    print(LOAD_HELP)
    print(QUIT_HELP)
    print()
    print("Output list:")
    print(OUTPUT_0_HELP)
    print(OUTPUT_1_HELP)
