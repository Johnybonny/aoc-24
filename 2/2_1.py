

def read_file(filename):
	with open(filename, "r") as file:
		reports = []
		for line in file:
			parsed_line = []
			for level in line.split():
				parsed_line.append(int(level))
			reports.append(parsed_line)
	return reports


def compute_safe_reports(reports):
	count = 0
	for report in reports:
		safe = True
		increasing = report[1] - report[0] > 0
		for i in range(len(report) - 1):
			if increasing and (report[i + 1] - report[i] < 1 or report[i + 1] - report[i] > 3):
				safe = False
				break
			if not increasing and (report[i] - report[i + 1] < 1 or report[i] - report[i + 1] > 3):
				safe = False
				break

		if safe:
			count += 1

	return count


def main():
	reports = read_file("input.txt")
	result = compute_safe_reports(reports)
	print(result)

if __name__ == "__main__":
	main()