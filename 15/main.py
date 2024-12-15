def read_file(filename):
	moves = []
	warehouse_map = []
	with open(filename, "r") as file:
		for line in file:
			if line[0] == "#":
				if line[-1] == "\n":
					warehouse_map.append(list(line[:-1]))
			elif line[0] in ["<", ">", "v", "^"]:
				if line[-1] == "\n":
					line = line[:-1]
				for move in list(line):
					if move == "<":
						moves.append([0, -1])
					elif move == ">":
						moves.append([0, 1])
					elif move == "v":
						moves.append([1, 0])
					elif move == "^":
						moves.append([-1, 0])

	robot = []
	for i in range(len(warehouse_map)):
		for j in range(len(warehouse_map[0])):
			if warehouse_map[i][j] == "@":
				robot = [i, j]
				warehouse_map[i][j] = "."

	return robot, moves, warehouse_map


def make_moves(robot, moves, warehouse_map):
	for move in moves:
		if warehouse_map[robot[0] + move[0]][robot[1] + move[1]] == ".":
			robot[0] += move[0]
			robot[1] += move[1]
		elif warehouse_map[robot[0] + move[0]][robot[1] + move[1]] == "#":
			pass
		elif warehouse_map[robot[0] + move[0]][robot[1] + move[1]] == "O":
			boxes_to_move = []
			current_check = [robot[0] + move[0], robot[1] + move[1]]
			will_move = True
			while True:
				if warehouse_map[current_check[0]][current_check[1]] == "#":
					will_move = False
					break
				elif warehouse_map[current_check[0]][current_check[1]] == "O":
					boxes_to_move.append(list(current_check))
					current_check[0] += move[0]
					current_check[1] += move[1]
				elif warehouse_map[current_check[0]][current_check[1]] == ".":
					break

			if will_move:
				robot[0] += move[0]
				robot[1] += move[1]

				for box in boxes_to_move[::-1]:
					warehouse_map[box[0] + move[0]][box[1] + move[1]] = "O"
					warehouse_map[box[0]][box[1]] = "."


def get_gps_sum(robot, moves, warehouse_map):
	make_moves(robot, moves, warehouse_map)

	sum = 0
	for i in range(len(warehouse_map)):
		for j in range(len(warehouse_map[0])):
			if warehouse_map[i][j] == "O":
				sum += i * 100 + j

	return sum


def main():
	# robot, moves, warehouse_map = read_file("example_small.txt")
	# robot, moves, warehouse_map = read_file("example_big.txt")
	robot, moves, warehouse_map = read_file("input.txt")

	print(get_gps_sum(robot, moves, warehouse_map))



if __name__ == "__main__":
	main()
