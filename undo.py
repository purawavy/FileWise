import json
from datetime import datetime

LOG_FILE = "logs/history.json"

def log_action(old, new):
    entry = {
        "old": old,
        "new": new,
        "time": datetime.now().isoformat()
    }

    try:
        with open(LOG_FILE, "r") as f:
            data = json.load(f)
    except:
        data = []

    data.append(entry)

    with open(LOG_FILE, "w") as f:
        json.dump(data, f, indent=2)
