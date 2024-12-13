

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
		for level_index in range(len(report)):
			new_report = report[:level_index] + report[level_index + 1:]

			safe = True
			increasing = new_report[1] - new_report[0] > 0
			for i in range(len(new_report) - 1):
				if increasing and (new_report[i + 1] - new_report[i] < 1 or new_report[i + 1] - new_report[i] > 3):
					safe = False
					break
				if not increasing and (new_report[i] - new_report[i + 1] < 1 or new_report[i] - new_report[i + 1] > 3):
					safe = False
					break

			if safe:
				if level_index != 0:
					print(report, new_report)
				count += 1
				break

	return count


def main():
	reports = read_file("input.txt")
	result = compute_safe_reports(reports)
	print(result)


if __name__ == "__main__":
	main()