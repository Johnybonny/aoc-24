

def read_file(filename):
	a = []
	b = []
	with open(filename, "r") as file:
		for line in file:
			a.append(int(line.split()[0]))
			b.append(int(line.split()[1]))
	return a, b


def compute_simmilarity(a, b):
	unique = set(a)

	sum = 0
	for number in unique:
		sum += number * a.count(number) * b.count(number)

	return sum


def main():
	a, b = read_file("input.txt")
	result = compute_simmilarity(a, b)
	print(result)

if __name__ == "__main__":
	main()