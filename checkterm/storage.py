#Saving and loading

import json
from pathlib import Path
from . import state, output

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DATA_FILE = DATA_DIR / "savedata.json"

def save():
    DATA_DIR.mkdir(exist_ok=True)

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(
            {
                "entries": state.entries,
                "checklists": state.checklists,
                "next_id": state.next_id,
                "next_id_checklist": state.next_id_checklist
            },
            f,
            indent=4,
            ensure_ascii=False
        )

    print(output.end, output.sucess)

def load():
    if not DATA_FILE.exists():
        print(output.end, output.invalid)
        return

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    state.entries = data.get("entries", [])
    state.next_id = data.get("next_id", 1)

    print(output.end, output.sucess)