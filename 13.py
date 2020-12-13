with open("13.txt") as file_obj:
    lines = [line.strip() for line in file_obj.readlines()]

start_time = int(lines[0])
bus_ids = [int(entry) for entry in lines[1].split(",") if entry != "x"]

min_time = start_time
min_bus = None

for bus_id in bus_ids:
    waiting_time = bus_id - (start_time % bus_id)
    if waiting_time < min_time:
        min_time = waiting_time
        min_bus = bus_id

print(min_time * min_bus)