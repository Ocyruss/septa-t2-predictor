import pandas as pd


routes = pd.read_csv("data/gtfs_static/routes.txt")
stop_times = pd.read_csv("data/gtfs_static/stop_times.txt")
stops = pd.read_csv("data/gtfs_static/stops.txt")
trips = pd.read_csv("data/gtfs_static/trips.txt")


filtered_trips = trips[trips["route_id"] == "T2"]
filtered_stop_times = stop_times[stop_times["trip_id"].isin(filtered_trips["trip_id"])]

print(filtered_stop_times.head())
print(len(filtered_stop_times))
# print(trips["route_id"].unique())