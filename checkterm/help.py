#Help texts

#Commands
add_entry = "add-entry - Add one entry and its optional description"
add_description = "add-description - Add/edit description of one existing entry"
edit_entry_name = "edit-entry-name - Edit one entry's name"
check_entry = "check-entry - See info of one entry"
complete_entry = "complete-entry - Complete one entry"
uncomplete_entry = "uncomplete-entry - Uncomplete one entry"
remove_entry = "remove-entry - Remove one entry"
list = "list - List all entries"
list_incomplete = "list-incomplete - List incomplete entries"
list_completed = "list-completed - List completed entries"
save = "save - Save checklist"
load = "load - Load checklist"
quit = "quit - Quit the program"

#Outputs
output_sucess = "0 - Sucess"
output_invalid = "1 - Error (invalid)"


def run():
    print("Open readme.md for more help on this project")
    print()
    print("Command list:")
    print(add_entry)
    print(add_description)
    print(check_entry)
    print(edit_entry_name)
    print(complete_entry)
    print(uncomplete_entry)
    print(remove_entry)
    print(list)
    print(list_incomplete)
    print(list_completed)
    print(save)
    print(load)
    print(quit)
    print()
    print("Output list:")
    print(output_sucess)
    print(output_invalid)