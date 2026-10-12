import pandas as pd
import json

file_path = "data/raw/2026_10_08/t2_snapshots.jsonl"

flattened_records = []

with open(file_path, "r") as file:
    for line in file:
        snapshot = json.loads(line)
        polled_timestamp = snapshot.get("polled_at")

        vehicle_list = snapshot.get("vehicles")

        for vehicle in vehicle_list:
            vehicle["polled_at"] = polled_timestamp
            flattened_records.append(vehicle)

live_df = pd.DataFrame(flattened_records)

filtered_live_df = live_df[
    (live_df["next_stop_id"].notna()) &
    (live_df["late"] != 998)
]

print(f"Original raw vehicle records: {len(live_df)}")
print(f"Active vehicles after filtering: {len(filtered_live_df)}")
print("\nSample of clean live data:")
print(filtered_live_df.head())