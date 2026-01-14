#Saving and loading

import json
from pathlib import Path
from . import state

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DATA_FILE = DATA_DIR / "entries.json"

OUTPUT_END = "Operação concluída com output"
OUTPUT_SUCCESS = 0
OUTPUT_INVALID = 1

def save():
    DATA_DIR.mkdir(exist_ok=True)

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(state.entries, f, indent=4, ensure_ascii=False)

    print(OUTPUT_END, OUTPUT_SUCCESS)

def load():
    if not DATA_FILE.exists():
        print(OUTPUT_END, OUTPUT_INVALID)
        return

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        state.entries = json.load(f)

    print(OUTPUT_END, OUTPUT_SUCCESS)