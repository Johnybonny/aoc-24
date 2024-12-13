import copy

def read_file(filename):
	map = []
	with open(filename, "r") as file:
		data = file.readlines()
		for row in range(len(data)):
			map_row = []
			for column in range(len(data[row])):
				if data[row][column] == "^":
					guard = {"row": row, "column": column, "next_row": row - 1, "next_column": column}
					map_row.append(1)
				elif data[row][column] == ".":
					map_row.append(0)
				elif data[row][column] == "#":
					map_row.append("#")
			map.append(map_row)
	return map, guard


def get_new_guard_direction(guard):
	if guard["row"] - guard["next_row"] > 0:
		guard["next_column"] = guard["next_column"] + 1
		guard["next_row"] = guard["row"]
	elif guard["row"] - guard["next_row"] < 0:
		guard["next_column"] = guard["next_column"] - 1
		guard["next_row"] = guard["row"]
	elif guard["column"] - guard["next_column"] > 0:
		guard["next_row"] = guard["next_row"] - 1
		guard["next_column"] = guard["column"]
	elif guard["column"] - guard["next_column"] < 0:
		guard["next_row"] = guard["next_row"] + 1
		guard["next_column"] = guard["column"]

	return guard


def get_new_guard_position(guard):
	new_guard = dict(guard)

	new_guard["row"] = guard["next_row"]
	new_guard["column"] = guard["next_column"]
	new_guard["next_row"] = guard["next_row"] + guard["next_row"] - guard["row"]
	new_guard["next_column"] = guard["next_column"] + guard["next_column"] - guard["column"]

	return new_guard


def simulate_guard(map, guard):
	while 0 <= guard["next_row"] < len(map) and 0 <= guard["next_column"] < len(map[0]):
		if map[guard["next_row"]][guard["next_column"]] == "#":
			guard = get_new_guard_direction(guard)
		else:
			guard = get_new_guard_position(guard)

		map[guard["row"]][guard["column"]] = 1
	return map


def count_positions(map, guard):
	map = simulate_guard(map, guard)
	count = 0
	for i in range(len(map)):
		for j in range(len(map[i])):
			count += map[i][j] if map[i][j] != "#" else 0

	return count


def check_guard_cycle(map, guard):
	guard_positions = []
	guard_positions.append(list(guard.values()))
	while 0 <= guard["next_row"] < len(map) and 0 <= guard["next_column"] < len(map[0]):
		if map[guard["next_row"]][guard["next_column"]] == "#":
			guard = get_new_guard_direction(guard)
		else:
			guard = get_new_guard_position(guard)

		map[guard["row"]][guard["column"]] = 1
		if list(guard.values()) in guard_positions:
			return True
		else:
			guard_positions.append(list(guard.values()))

	return False


def count_obstructions(map, guard):
	no_obstructions_map = simulate_guard(map, guard)

	count = 0
	for i in range(len(map)):
		for j in range(len(map[i])):
			if no_obstructions_map[i][j] == 1:
				obstructed_map = copy.deepcopy(map)
				obstructed_map[i][j] = "#"
				new_guard = dict(guard)
				if check_guard_cycle(obstructed_map, new_guard):
					count += 1
	return count


def main():
	# start_map, start_guard = read_file("test.txt")
	start_map, start_guard = read_file("input.txt")
	map1 = copy.deepcopy(start_map)
	map2 = copy.deepcopy(start_map)
	guard1 = dict(start_guard)
	guard2 = dict(start_guard)

	print(count_positions(map1, guard1))
	print(count_obstructions(map2, guard2))


if __name__ == "__main__":
	main()
