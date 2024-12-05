
def read_file(filename):
	data = []
	with open(filename, "r") as file:
		for line in file:
			if line[-1:] == "\n":
				line = line[:-1]
			data.append(list(line))
	return data


def count_xmas_in_text(text):
	return text.count("XMAS") + text[::-1].count("XMAS")


def count_horizontal(puzzle):
	count = 0
	for row in puzzle:
		line = "".join(row)
		count += count_xmas_in_text(line)
	return count


def count_vertical(puzzle):
	count = 0
	for column_index in range(len(puzzle[0])):
		column = ""
		for row_index in range(len(puzzle)):
			column += puzzle[row_index][column_index]

		count += count_xmas_in_text(column)
	return count


def count_diagonal(puzzle):
	count = 0

	# / direction
	start_row = 0
	start_column = 0
	while start_column < len(puzzle[0]):
		current_row = start_row
		current_column = start_column

		text = ""
		while current_row >= 0 and current_column <= len(puzzle[0]) - 1:
			text += puzzle[current_row][current_column]
			current_row -= 1
			current_column += 1

		count += count_xmas_in_text(text)

		if start_row < len(puzzle) - 1:
			start_row += 1
		else:
			start_column += 1

	# \ direction
	start_row = len(puzzle) - 1
	start_column = 0
	while start_column < len(puzzle[0]):
		current_row = start_row
		current_column = start_column

		text = ""
		while current_row <= len(puzzle) - 1 and current_column <= len(puzzle[0]) - 1:
			text += puzzle[current_row][current_column]
			current_row += 1
			current_column += 1

		count += count_xmas_in_text(text)

		if start_row > 0:
			start_row -= 1
		else:
			start_column += 1

	return count


def count_xmas(puzzle):
	return count_horizontal(puzzle) + count_vertical(puzzle) + count_diagonal(puzzle)


def get_puzzle_fragment(puzzle, row, column):
	fragment = []
	for i in range(3):
		fragment.append(puzzle[row + i][column:column + 3])
	return fragment


def count_x_mas(puzzle):
	count = 0
	for row_index in range(len(puzzle) - 2):
		for column_index in range(len(puzzle[0]) - 2):
			fragment = get_puzzle_fragment(puzzle, row_index, column_index)
			diagonal_1 = "".join([fragment[0][0], fragment[1][1], fragment[2][2]])
			diagonal_2 = "".join([fragment[0][2], fragment[1][1], fragment[2][0]])

			if diagonal_1 == "MAS" or diagonal_1[::-1] == "MAS":
				if diagonal_2 == "MAS" or diagonal_2[::-1] == "MAS":
					count += 1

	return count


def main():
	# data = read_file("test.txt")
	data = read_file("input.txt")

	print(count_xmas(data)) # First star
	print(count_x_mas(data)) # Second star


if __name__ == "__main__":
	main()
