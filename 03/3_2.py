import re

def read_file(filename):
	instructions = []
	with open(filename, "r") as file:
		for line in file:
			instructions.append(line)
	return instructions


def sum_multiplications(instructions):
	sum = 0
	enabled = True
	for instruction in instructions:
		matches = re.findall("mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", instruction)
		for match in matches:
			if match == "do()":
				enabled = True
			elif match == "don't()":
				enabled = False
			elif enabled:
				numbers = match[4:-1].split(",")
				sum += int(numbers[0]) * int(numbers[1])

	return sum


def main():
	instructions = read_file("input.txt")
	result = sum_multiplications(instructions)
	print(result)


if __name__ == "__main__":
	main()