import requests
import json
from datetime import datetime
from pathlib import Path
import time

def request_breakdown():
    
    try:
        response = requests.get("https://www3.septa.org/api/TransitView/index.php?route=T2")
        data = response.json()
        if isinstance(data, dict):
            trolley = data.get("bus")
            return trolley
        else:
            print(f"Unexpected response format: {type(data)}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Netword request failed: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Failed to parse into JSON: {e}")
        return None

def snapshot_save(vehicles):
    if vehicles is None:
        return
        
    today = datetime.now().strftime("%Y_%m_%d")
    
    folder = Path("data") / "raw" / today

    folder.mkdir(parents=True, exist_ok=True)

    outfile = folder / "t2_snapshots.jsonl"

    record = {
        "polled_at": datetime.now().isoformat(), 
        "vehicles": vehicles
    }

    json_string = json.dumps(record)

    with open(outfile,"a") as f:
        f.write(json_string + "\n")


if __name__ == "__main__":
    while True:
        trolley = request_breakdown()
        snapshot_save(trolley)
        if trolley is None:
            print("Polling failure")
        else:
            print(len(trolley))
        time.sleep(60)