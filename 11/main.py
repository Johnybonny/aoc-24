def read_file(filename):
	stones = []
	with open(filename, "r") as file:
		stones = file.readline().split(" ")
		if stones[-1][-1] == "\n":
			stones[-1] = stones[-1][:-1]
	return stones


def get_stones_number(stones, blinks_number):
	for _ in range(blinks_number):
		new_stones = []
		for stone in stones:
			if stone == "0":
				new_stones.append("1")
			elif len(stone) % 2 == 0:
				new_stones.append(str(int(stone[:len(stone) // 2])))
				new_stones.append(str(int(stone[len(stone) // 2:])))
			else:
				new_stones.append(str(int(stone) * 2024))
		stones = new_stones
	return len(stones)


def main():
	# stones = read_file("test.txt")
	stones = read_file("input.txt")

	print(get_stones_number(stones, 25)) # First star

	# print(get_stones_number(stones, 75)) # Second star
	# # To be continued


if __name__ == "__main__":
	main()
