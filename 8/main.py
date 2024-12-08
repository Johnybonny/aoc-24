from collections import Counter

def read_file(filename):
	map = []
	with open(filename, "r") as file:
		for line in file:
			row = list(line)
			if row[-1] == "\n":
				row = row[:-1]
			map.append(row)

	antennas = {}
	size = [len(map), len(map[0])]
	for i in range(size[0]):
		for j in range(size[1]):
			if map[i][j] == ".":
				pass
			elif map[i][j] in antennas.keys():
				antennas[map[i][j]].append([i, j])
			else:
				antennas[map[i][j]] = [[i, j]]

	return antennas, size


def get_uniques_length(list):
	unique = []
	for element in list:
		if element not in unique:
			unique.append(element)
	return len(unique)


def find_antinode(first_node, second_node, size, all_antinodes):
	new_row = first_node[0] + first_node[0] - second_node[0]
	new_column = first_node[1] + first_node[1] - second_node[1]

	if 0 <= new_row < size[0] and 0 <= new_column < size[1]:
		all_antinodes.append([new_row, new_column])


def find_all_antinodes(first_node, second_node, size, antinodes):
	new_point = [first_node[0] + first_node[0] - second_node[0],
			  first_node[1] + first_node[1] - second_node[1]]
	prev_point = first_node
	while 0 <= new_point[0] < size[0] and 0 <= new_point[1] < size[1]:
		antinodes.append(new_point)
		tmp = new_point
		new_point = [tmp[0] + tmp[0] - prev_point[0],
			tmp[1] + tmp[1] - prev_point[1]]
		prev_point = tmp

	antinodes.append(first_node)
	antinodes.append(second_node)


def count_antinodes(antennas, size):
	singular_antinodes = []
	all_antinodes = []
	for _, nodes in antennas.items():
		for i in range(len(nodes)):
			for j in range(len(nodes)):
				if i != j:
					find_antinode(nodes[i], nodes[j], size, singular_antinodes)
					find_all_antinodes(nodes[i], nodes[j], size, all_antinodes)

	return get_uniques_length(singular_antinodes), get_uniques_length(all_antinodes)


def main():
	# antennas, size = read_file("test.txt")
	antennas, size = read_file("input.txt")

	first_answer, second_answer = count_antinodes(antennas, size)
	print(first_answer)
	print(second_answer)


if __name__ == "__main__":
	main()
