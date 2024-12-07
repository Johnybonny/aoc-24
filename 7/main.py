def read_file(filename):
	test_values = []
	equations = []
	with open(filename, "r") as file:
		for line in file:
			test_values.append(int(line.split(":")[0]))
			equation = []
			for number in line.split(":")[1].split(" ")[1:]:
				equation.append(int(number))
			equations.append(equation)

	return test_values, equations


"""
row and column correspond to rows and columns in matrix of all possible configurations.
Example for equation with 3 operators, eg. 7290: 6 8 6 15
	0	1	2
0	+	+	+
1	+	+	*
2	+	*	+
3	+	*	*
4	*	+	+
5	*	+	*
6	*	*	+
7	*	*	*
"""
def is_equation_possible(test_value, equation):
	num_of_operators = len(equation) - 1
	for row in range(2 ** num_of_operators):
		result = equation[0]
		for number_index in range(1, len(equation)):
			column = number_index - 1
			if row // ( 2 ** (num_of_operators - 1 - column)) % 2 == 0:
				result += equation[number_index]
			else:
				result *= equation[number_index]

			if result > test_value: # Already too big
				break
		if result == test_value:
			return True
	return False


def sum_results(test_values, equations):
	sum = 0
	for i in range(len(test_values)):
		if is_equation_possible(test_values[i], equations[i]):
			sum += test_values[i]
	return sum


"""
Modified version has 3 types of operators.
"""
def is_equation_possible_2(test_value, equation):
	num_of_different_operators = 3
	num_of_operators = len(equation) - 1
	for row in range(num_of_different_operators ** num_of_operators):
		result = equation[0]
		for number_index in range(1, len(equation)):
			column = number_index - 1
			modulo = row // ( num_of_different_operators ** (num_of_operators - 1 - column)) % num_of_different_operators
			if modulo == 0:
				result += equation[number_index]
			elif modulo == 1:
				result *= equation[number_index]
			else:
				result = int(str(result) + str(equation[number_index]))

			if result > test_value: # Already too big
				break
		if result == test_value:
			return True
	return False


def sum_results_2(test_values, equations):
	sum = 0
	for i in range(len(test_values)):
		if is_equation_possible_2(test_values[i], equations[i]):
			sum += test_values[i]
	return sum


def main():
	# test_values, equations = read_file("test.txt")
	test_values, equations = read_file("input.txt")

	print(sum_results(test_values, equations))
	print(sum_results_2(test_values, equations))


if __name__ == "__main__":
	main()
