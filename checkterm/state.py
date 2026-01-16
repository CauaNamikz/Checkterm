#State

#Import from commands
from . import commands

#State for entries
entries = []

next_id = 1

def get_next_id():
    global next_id
    current = next_id
    next_id += 1
    return current

#State for checklists
checklistname = 1
checklistdesc = 1

checklists = []

next_id_checklist = 1

def get_next_id_checklist():
    global next_id_checklist
    current_cl = next_id_checklist
    next_id_checklist += 1
    return current_cl