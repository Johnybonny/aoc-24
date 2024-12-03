

def read_file(filename):
	a = []
	b = []
	with open(filename, "r") as file:
		for line in file:
			a.append(int(line.split()[0]))
			b.append(int(line.split()[1]))
	return a, b


def compute_differences(a, b):
	a.sort()
	b.sort()

	sum = 0
	for i in range(len(a)):
		sum += abs(a[i] - b[i])
	return sum


def main():
	a, b = read_file("input.txt")
	result = compute_differences(a, b)
	print(result)

if __name__ == "__main__":
	main()