
def read_file(filename):
	rules = []
	updates = []
	with open(filename, "r") as file:
		for line in file:
			if "|" in line:
				rules.append([int(x) for x in line.split("|")])
			elif line != "\n":
				updates.append([int(x) for x in line.split(",")])
	return rules, updates


def fix_update(rules, update):
	filtered_rules = []
	for rule in rules:
		if rule[0] in update and rule[1] in update:
			filtered_rules.append(rule)

	behind_pages = {u: set() for u in update}
	for filtered_rule in filtered_rules:
		behind_pages[filtered_rule[0]].add(filtered_rule[1])

	fixed = []
	for key, behind in behind_pages.items():
		earliest_index = len(fixed)
		for page in behind:
			if page in fixed:
				if fixed.index(page) < earliest_index:
					earliest_index = fixed.index(page)
		fixed.insert(earliest_index, key)

	return fixed


def sum_page_numbers(rules, updates):
	correct_sum = 0
	fixed_sum = 0
	for update in updates:
		correct = True
		for rule in rules:
			try:
				first_index = update.index(rule[0])
				second_index = update.index(rule[1])
				if first_index >= second_index:
					correct = False
					break
			except ValueError: # Update doesn't include one or both pages
				pass
		if correct:
			correct_sum += update[len(update) // 2]
		else:
			fixed_update = fix_update(rules, update)
			fixed_sum += fixed_update[len(update) // 2]

	return correct_sum, fixed_sum

def main():
	# rules, updates = read_file("test.txt")
	rules, updates = read_file("input.txt")

	correct, fixed = sum_page_numbers(rules, updates)
	print(correct) # First star
	print(fixed) # Second star


if __name__ == "__main__":
	main()
