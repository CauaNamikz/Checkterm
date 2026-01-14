#Dictionary state

entries = []

next_id = 1

def get_next_id():
    global next_id
    current = next_id
    next_id += 1
    return current