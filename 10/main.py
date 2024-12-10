def read_file(filename):
	map = []
	with open(filename, "r") as file:
		for line in file:
			if line[-1] == "\n":
				row = line[:-1]
			else:
				row = line
			map_row = [int(i) for i in row]
			map.append(map_row)
	return map


def get_trailhead_peaks(map, row, column):
	if map[row][column] == 9:
		return [[row, column]]
	else:
		peaks = []
		wanted_height = map[row][column] + 1
		if row > 0 and map[row - 1][column] == wanted_height: # up
			peaks += get_trailhead_peaks(map, row - 1, column)
		if row < len(map) - 1 and map[row + 1][column] == wanted_height: # down
			peaks += get_trailhead_peaks(map, row + 1, column)
		if column > 0 and map[row][column - 1] == wanted_height: # left
			peaks += get_trailhead_peaks(map, row, column - 1)
		if column < len(map[0]) - 1 and map[row][column + 1] == wanted_height: # right
			peaks += get_trailhead_peaks(map, row, column + 1)

		return peaks


def get_number_of_unique_peaks(peaks):
	unique = []
	for peak in peaks:
		if peak not in unique:
			unique.append(peak)
	return len(unique)


def get_trailhead_rating(map, row, column):
	if map[row][column] == 9:
		return 1
	else:
		rating = 0
		wanted_height = map[row][column] + 1
		if row > 0 and map[row - 1][column] == wanted_height: # up
			rating += get_trailhead_rating(map, row - 1, column)
		if row < len(map) - 1 and map[row + 1][column] == wanted_height: # down
			rating += get_trailhead_rating(map, row + 1, column)
		if column > 0 and map[row][column - 1] == wanted_height: # left
			rating += get_trailhead_rating(map, row, column - 1)
		if column < len(map[0]) - 1 and map[row][column + 1] == wanted_height: # right
			rating += get_trailhead_rating(map, row, column + 1)

		return rating


def get_trailheads_sums(map):
	scores_sum = 0
	ratings_sum = 0
	for row in range(len(map)):
		for column in range(len(map[0])):
			if map[row][column] == 0:
				scores_sum += get_number_of_unique_peaks(get_trailhead_peaks(map, row, column))
				ratings_sum += get_trailhead_rating(map, row, column)
	return scores_sum, ratings_sum


def main():
	# map = read_file("test.txt")
	map = read_file("input.txt")

	scores_sum, ratings_sum = get_trailheads_sums(map)
	print(scores_sum)
	print(ratings_sum)


if __name__ == "__main__":
	main()
