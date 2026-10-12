import pandas as pd


routes = pd.read_csv("data/gtfs_static/routes.txt")
stop_times = pd.read_csv("data/gtfs_static/stop_times.txt")
stops = pd.read_csv("data/gtfs_static/stops.txt")
trips = pd.read_csv("data/gtfs_static/trips.txt")


filtered_trips = trips[trips["route_id"] == "T2"]
filtered_stop_times = stop_times[stop_times["trip_id"].isin(filtered_trips["trip_id"])]


t2_schedule = pd.merge(
    filtered_stop_times,
    stops[['stop_id', 'stop_name', 'stop_lat', 'stop_lon']],
    on='stop_id',
    how='left'
)

t2_schedule = t2_schedule.sort_values(by=['trip_id', 'stop_sequence'])

print(t2_schedule[['trip_id', 'stop_name', 'arrival_time', 'stop_sequence']].head(10))