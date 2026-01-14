#Base of commands for CLI

from . import state

OUTPUT_END = "Task finished with output"
OUTPUT_SUCCESS = 0
OUTPUT_INVALID = 1


# Help texts
ADD_ENTRY_HELP = "add-entry - Add entries "
COMPLETE_ENTRY_HELP = "complete-entry - Complete entries"
REMOVE_ENTRY_HELP = "remove-entry - Remove entries"
SAVE_HELP = "save - Save checklist"
LOAD_HELP = "load - Load checklist"
LIST_ACTIVE_HELP = "list-active - See list of active entries"
LIST_STATE_0_HELP = "list-state-0 - See list of incomplete entries"
LIST_STATE_1_HELP = "list-state-1 - See list of completed entries"
QUIT_HELP = "quit - Quit the program"

OUTPUT_0_HELP = "0 - sucess"
OUTPUT_1_HELP = "1 - error (invalid)"


# Commands
def add_entry():
    name = input("Entry name > ")

    if name.strip() == "":
        print(OUTPUT_END, OUTPUT_INVALID)
        return

    state.entries.append({
        "id": state.get_next_id(),
        "name": name,
        "active": 1,
        "state": 0
    })

    print(OUTPUT_END, OUTPUT_SUCCESS)


def complete_entry():
    try:
        id_ = int(input("ID for next completed entry (get with list-active) > "))
    except ValueError:
        print(OUTPUT_END, OUTPUT_INVALID)
        return

    for entry in state.entries:
        if entry["id"] == id_:
            entry["state"] = 1
            entry["active"] = 0
            print(OUTPUT_END, OUTPUT_SUCCESS)
            return

    print(OUTPUT_END, OUTPUT_INVALID)


def remove_entry():
    try:
        id_ = int(input("ID for next removed entry (get with list-active) > "))
    except ValueError:
        print(OUTPUT_END, OUTPUT_INVALID)
        return

    for i, entry in enumerate(state.entries):
        if entry["id"] == id_:
            del state.entries[i]
            print(OUTPUT_END, OUTPUT_SUCCESS)
            return

    print(OUTPUT_END, OUTPUT_INVALID)


def list_active():
    print("Active entries:")
    for entry in state.entries:
        print("ID", entry["id"], "-", entry["name"])


def list_state_0():
    print("Incomplete entries:")
    for entry in state.entries:
        if entry["state"] == 0:
            print("ID", entry["id"], "-", entry["name"])


def list_state_1():
    print("Complete entries:")
    for entry in state.entries:
        if entry["state"] == 1:
            print("ID", entry["id"], "-", entry["name"])


def help_command():
    print("Command list:")
    print(ADD_ENTRY_HELP)
    print(COMPLETE_ENTRY_HELP)
    print(REMOVE_ENTRY_HELP)
    print(LIST_ACTIVE_HELP)
    print(LIST_STATE_0_HELP)
    print(LIST_STATE_1_HELP)
    print(SAVE_HELP)
    print(LOAD_HELP)
    print(QUIT_HELP)
    print()
    print("Output list:")
    print(OUTPUT_0_HELP)
    print(OUTPUT_1_HELP)
