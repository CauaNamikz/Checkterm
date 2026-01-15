#Base of commands for CLI

#Import from state.py
from . import state, output


# Commands
def list(): #List current entries
    print("Entradas atuais:")
    for entry in state.entries:
        print("ID", entry["id"], "-", entry["name"])


def add_entry(): #Add one entry
    name = input("Entry name > ")

    if name.strip() == "":
        print(output.end, output.invalid)
        return
    
    desc = input("Entry description (optional) > ")

    state.entries.append({
        "id": state.get_next_id(),
        "name": name,
        "description": desc,
        "completed": 0
    })

    print(output.end, output.sucess)


def add_description(): #Add description to existing entry
    list()
    id_ = int(input("ID of entry to be given a description > "))

    for entry in state.entries:
        if entry["id"] == id_:
            entry["description"] = input("Description > ")
            print(output.end, output.sucess)
        else:
            print(output.end, output.invalid)


def check_entry(): #List one entry's info
    list()
    id_ = int(input("ID of entry to be checked > "))
    
    for entry in state.entries:
        if entry["id"] == id_:
            print(entry["name"])
            print("ID", entry["id"])
            print(entry["description"])
        else:
            (output.end, output.invalid)


def edit_entry_name(): #Edit one entry's name
    list()
    id_ = int(input("ID of entry to be given a description > "))

    for entry in state.entries:
        if entry["id"] == id_:
            entry["name"] = input("Name > ")
            print(output.end, output.sucess)
        else:
            print(output.end, output.invalid)


def complete_entry(): #Complete one entry
    list()
    id_ = int(input("ID of entry to be completed > "))

    for entry in state.entries:
        if entry["id"] == id_:
            entry["completed"] = 1
            print(output.end, output.invalid)
            return
        else:
            print(output.end, output.invalid)


def uncomplete_entry(): #Uncomplete one entry
    list()
    id_ = int(input("ID of entry to be uncompleted > "))

    for entry in state.entries:
        if entry["id"] == id_:
            entry["completed"] = 0
            print(output.end, output.sucess)
            return
        else:
            print(output.end, output.invalid)


def remove_entry(): #Remove one entry
    list()
    id_ = int(input("ID of entry to be removed > "))

    for entry in state.entries:
        if entry["id"] == id_:
            state.entries.remove
            print(output.end, output.sucess)
            return
        else:
            print(output.end, output.invalid)


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
