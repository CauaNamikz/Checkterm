#Base of commands for CLI


#Import from state.py
from . import state, output


# Commands
def list(): #List current entries
    print("Entradas atuais:")
    for entry in state.entries:
        print("ID", entry["id"], "-", entry["name"])


def list_checklists(): #List current checklists
    for checklist in state.checklists:
        print("ID", checklist["id"], "-", checklist["name"])


def add_checklist(): #Add one checklist
    state.checklistname = input("Create checklist name > ")

    if state.checklistname.strip == "":
        print(output.end, output.invalid)
        return
    else:
        state.checklistdesc = input("Create checklist description (optional) > ")
        state.checklists.append({
            "id": state.get_next_id_checklist(),
            "name": state.checklistname,
            "description": state.checklistdesc
        })
        print(output.end, output.sucess)


def add_entry(): #Add one entry
    if state.checklistname != 1:
        checklist_id = int(input("Assign this entry to checklist ID > "))
        name = input("Entry name > ")
        if name.strip() == "":
            print(output.end, output.invalid)
            return
        else:
            desc = input("Entry description (optional) > ")

            state.entries.append({
                "id": state.get_next_id(),
                "name": name,
                "description": desc,
                "completed": False,
                "checklist": {
                    "id": checklist_id,
                    "name": state.checklistname,
                    "description": state.checklistdesc
                } 
            })

            print(output.end, output.sucess)
    else:
        print("You have to create a checklist.")
        print(output.end, output.invalid)


def edit_checklist_name():
    list_checklists()
    id_c = int(input("ID of checklist to have name edited > "))

    for checklist in state.checklists:
        if checklist["id"] == id_c:
            name_c = input("Name > ")
            checklist["name"] = name_c
            for info in state.entries:
                info["checklist"]["name"] = name_c
            print(output.end, output.sucess)
        else:
            print(output.end, output.invalid)


def edit_checklist_description():
    list_checklists()
    id_c = int(input("ID of checklist to have description edited > "))

    for checklist in state.checklists:
        if checklist["id"] == id_c:
            name_c = input("Description > ")
            checklist["description"]
            for info in state.entries:
                info["checklist"]["description"]
            print(output.end, output.sucess)
        else:
            print(output.end, output.invalid)


def edit_entry_description(): #Add/edit description to existing entry
    list()
    id_ = int(input("ID of entry to have description edited/added > "))

    for entry in state.entries:
        if entry["id"] == id_:
            entry["description"] = input("Description > ")
            print(output.end, output.sucess)
        else:
            print(output.end, output.invalid)


def check_entry(): #List one entry's info
    id_ = int(input("ID of entry to be checked > "))
    
    for entry in state.entries:
        if entry["id"] == id_:
            print("ID", entry["id"])
            print(entry["name"])
            print(entry["description"])
            print("Completed:", entry["completed"])
        else:
            (output.end, output.invalid)


def check_checklist(): #List one checklist's info 
    id_c = int(input("ID of checklist to be checked > "))
    for entry in state.entries:
        if entry["id"] == id_c:
            print("ID", entry["id"])
            print(entry["name"])
            print(entry["description"])
            print("Completed:", entry["completed"])
        else:
            (output.end, output.invalid)


def edit_entry_name(): #Edit one entry's name
    list()
    id_ = int(input("ID of entry to have name edited > "))

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
            entry["completed"] = True
            print(output.end, output.invalid)
            return
        else:
            print(output.end, output.invalid)


def uncomplete_entry(): #Uncomplete one entry
    list()
    id_ = int(input("ID of entry to be uncompleted > "))

    for entry in state.entries:
        if entry["id"] == id_:
            entry["completed"] = False
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
        if entry["completed"] == False:
            print("ID", entry["id"], "-", entry["name"])
        else:
            print("No entries incomplete.")


def list_completed(): #List complete entries
    print("Complete entries:")
    for entry in state.entries:
        if entry["completed"] == True:
            print("ID", entry["id"], "-", entry["name"])
        else:
            print("No entries completed.")


def list_checklist_entries(): #List all entries of one checklist
    id_c = input("ID of checklist to have all its entries listed > ")

    for entry in state.entries:
        if entry["checklist"]["id"] == id_c:
            print("Checklist", entry["checklist"]["name"])
            print()
            print("ID", entry["id"])
            print(entry["name"])
            print(entry["description"])
            print("Completed:", entry["completed"])