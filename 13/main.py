def read_file(filename):
	games = []
	game = {}
	with open(filename, "r") as file:
		for line in file:
			line = line.split(":")
			if line[0][:-2] == "Button":
				values = line[1].split(",")
				game[line[0][-1]] = [int(values[0].split("+")[1]), int(values[1].split("+")[1])]
			elif line[0] == "Prize":
				values = line[1].split(",")
				game[line[0]] = [int(values[0].split("=")[1]), int(values[1].split("=")[1])]
				games.append(game)
				game = {}

	return games


def determinant(matrix):
	return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def winning_game_cost(game):
	a_cost = 3
	b_cost = 1
	matrix = [[game["A"][0], game["B"][0], game["Prize"][0]],
		   [game["A"][1], game["B"][1], game["Prize"][1]]]
	w = determinant([[matrix[0][0], matrix[0][1]], [matrix[1][0], matrix[1][1]]])
	w_a = determinant([[matrix[0][2], matrix[0][1]], [matrix[1][2], matrix[1][1]]])
	w_b = determinant([[matrix[0][0], matrix[0][2]], [matrix[1][0], matrix[1][2]]])

	if w != 0:
		a = w_a / w
		b = w_b / w
		if a % 1 == 0 and b % 1 == 0:
			return a * a_cost + b * b_cost
		else:
			return 0


def count_winnable_games_tokens(games):
	sum = 0
	for game in games:
		cost = winning_game_cost(game)
		sum += cost
	return int(sum)


def update_prizes_location(games, update_amount):
	for game in games:
		game["Prize"][0] += update_amount
		game["Prize"][1] += update_amount


def main():
	# games = read_file("test.txt")
	games = read_file("input.txt")

	print(count_winnable_games_tokens(games))

	update_prizes_location(games, 10_000_000_000_000)
	print(count_winnable_games_tokens(games))


if __name__ == "__main__":
	main()
