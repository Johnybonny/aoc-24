def read_file(filename):
	with open(filename, "r") as file:
		line = file.readline()
		if line[-1] == "\n":
			line = line[:-1]
		return line


def convert_map_to_layout(disk_map):
	layout = []
	id = 0
	file_space = True
	for i in range(len(disk_map)):
		if file_space:
			layout += [id] * int(disk_map[i])
			id += 1
		else:
			layout += ["."] * int(disk_map[i])
		file_space = not file_space
	return layout


def move_file_blocks(layout):
	left = 0
	right = len(layout) - 1
	while left < right:
		if layout[left] == "." and layout[right] != ".":
			layout[left], layout[right] = layout[right], layout[left]
			left += 1
			right -= 1
		else:
			if layout[left] != ".":
				left += 1
			if layout[right] == ".":
				right -= 1


def compute_checksum(layout):
	checksum = 0
	for i in range(len(layout)):
		if layout[i] == ".":
			pass
		else:
			checksum += i * layout[i]
	return checksum


def first_star(disk_map):
	layout = convert_map_to_layout(disk_map)
	move_file_blocks(layout)
	checksum = compute_checksum(layout)
	return checksum


def convert_map_to_compact(disk_map):
	compact = []
	id = 0
	file_space = True
	for i in range(len(disk_map)):
		if file_space:
			compact.append([id, int(disk_map[i])])
			id += 1
		else:
			compact.append([".", int(disk_map[i])])
		file_space = not file_space

	without_zeros = []
	for element in compact:
		if element[1] != 0:
			without_zeros.append(element)

	return without_zeros


def move_whole_file_blocks(compact_layout):
	right = len(compact_layout) - 1
	while right > 0:
		file = list(compact_layout[right])
		if file[0] != ".":
			left = 0
			found_new_place = False
			for left in range(right):
				place = list(compact_layout[left])
				if place[0] == "." and place[1] >= file[1]:
					# Update previous empty space
					compact_layout.pop(left)
					elements_added = 0
					if place[1] > file[1]:
						compact_layout.insert(left, [".", place[1] - file[1]])
						elements_added = 1
					compact_layout.insert(left, file)

					right += elements_added

					# Merge empty file spaces next to each other, eg ..777...
					if right - 1 > 0 and compact_layout[right - 1][0] == "." and right + 1 < len(compact_layout) and compact_layout[right + 1][0] == ".":
						medium_dots = compact_layout.pop(right)[1]
						right_dots = compact_layout.pop(right)[1]
						compact_layout[right - 1][1] += medium_dots + right_dots # right + 1, because indices were modified
						right -= 2
					elif right - 1 > 0 and compact_layout[right - 1][0] == ".": # eg. ..777888
						medium_dots = compact_layout.pop(right)[1]
						compact_layout[right - 1][1] += medium_dots
						right -= 2
					elif right + 1 < len(compact_layout) and compact_layout[right + 1][0] == ".":
						right_dots = compact_layout.pop(right)[1] # eg. 6777...
						compact_layout[right][1] += right_dots
						right -= 1
					else: # eg. 667778
						compact_layout[right][0] = "."
						right -= 1

					found_new_place = True
					break
			if not found_new_place:
				right -= 1
		else:
			right -= 1


def convert_to_traditional(compact_layout):
	layout = []
	for c in compact_layout:
		layout += [c[0]] * c[1]
	return layout


def second_star(disk_map):
	compact_layout = convert_map_to_compact(disk_map)
	move_whole_file_blocks(compact_layout)
	layout = convert_to_traditional(compact_layout)
	checksum = compute_checksum(layout)

	return checksum


def main():
	# disk_map = read_file("test.txt")
	disk_map = read_file("input.txt")

	print(first_star(disk_map))
	print(second_star(disk_map))


if __name__ == "__main__":
	main()
