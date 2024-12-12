def read_file(filename):
	map = []
	with open(filename, "r") as file:
		for line in file:
			if line[-1] == "\n":
				line = line[:-1]
			map.append(list(line))
	return map


def find_region(map, plant_row, plant_column, region_plants):
	plant_type = map[plant_row][plant_column]
	if plant_row > 0 and map[plant_row - 1][plant_column] == plant_type and [plant_row - 1, plant_column] not in region_plants:
		region_plants.append([plant_row - 1, plant_column])
		find_region(map, plant_row - 1, plant_column, region_plants)
	if plant_row < len(map) - 1 and map[plant_row + 1][plant_column] == plant_type and [plant_row + 1, plant_column] not in region_plants:
		region_plants.append([plant_row + 1, plant_column])
		find_region(map, plant_row + 1, plant_column, region_plants)
	if plant_column > 0 and map[plant_row][plant_column - 1] == plant_type and [plant_row, plant_column - 1] not in region_plants:
		region_plants.append([plant_row, plant_column - 1])
		find_region(map, plant_row, plant_column - 1, region_plants)
	if plant_column < len(map[0]) - 1 and map[plant_row][plant_column + 1] == plant_type and [plant_row, plant_column + 1] not in region_plants:
		region_plants.append([plant_row, plant_column + 1])
		find_region(map, plant_row, plant_column + 1, region_plants)


def find_regions(map):
	regions = []
	for i in range(len(map)):
		for j in range(len(map[0])):
			if not is_point_in_some_region([i, j], regions):
				region = [[i, j]]
				find_region(map, i, j, region)
				regions.append(region)
	return regions


def is_point_in_some_region(point, regions):
	for region in regions:
		for plant in region:
			if plant == point:
				return True
	return False


def region_perimeter(region, map):
	plant_type = map[region[0][0]][region[0][1]]

	perimeter = 0
	for plant in region:
		plant_row = plant[0]
		plant_column = plant[1]
		if plant_row == 0 or map[plant_row - 1][plant_column] != plant_type:
			perimeter += 1
		if plant_row == len(map) - 1 or map[plant_row + 1][plant_column] != plant_type:
			perimeter += 1
		if plant_column == 0 or map[plant_row][plant_column - 1] != plant_type:
			perimeter += 1
		if plant_column == len(map[0]) - 1 or map[plant_row][plant_column + 1] != plant_type:
			perimeter += 1
	return perimeter


def compute_fencing_price(map):
	regions = find_regions(map)
	sum = 0
	for region in regions:
		sum += len(region) * region_perimeter(region, map)
	return sum


def get_region_furthest_points(region, map):
	left_top = [len(map[0]), len(map)]
	right_bottom = [0, 0]
	for plant in region:
		if plant[0] < left_top[0]:
			left_top[0] = plant[0]
		if plant[0] > right_bottom[0]:
			right_bottom[0] = plant[0]
		if plant[1] < left_top[1]:
			left_top[1] = plant[1]
		if plant[1] > right_bottom[1]:
			right_bottom[1] = plant[1]
	return left_top, right_bottom


def get_region_corners_number(region, map):
	corners = 0
	left_top, right_bottom = get_region_furthest_points(region, map)

	current_row = left_top[0]
	current_column = left_top[1]
	end_row = right_bottom[0] + 1
	end_column = right_bottom[1] + 1

	while current_row <= end_row:
		coordinates_in_region = 0
		if [current_row - 1, current_column - 1] in region:
			coordinates_in_region += 1
		if [current_row - 1, current_column] in region:
			coordinates_in_region += 1
		if [current_row, current_column - 1] in region:
			coordinates_in_region += 1
		if [current_row, current_column] in region:
			coordinates_in_region += 1

		if coordinates_in_region == 1 or coordinates_in_region == 3:
			corners += 1
		else:
			if (([current_row - 1, current_column - 1] in region
	   		and [current_row - 1, current_column] not in region
	   		and [current_row, current_column - 1] not in region
	   		and [current_row, current_column] in region)
			   or
			   ([current_row - 1, current_column - 1] not in region
	   		and [current_row - 1, current_column] in region
	   		and [current_row, current_column - 1] in region
	   		and [current_row, current_column] not in region)):
				corners += 2

		current_column += 1
		if current_column > end_column:
			current_row += 1
			current_column = 0

	return corners


def compute_bulk_fencing_price(map):
	regions = find_regions(map)
	sum = 0
	for region in regions:
		sum += len(region) * get_region_corners_number(region, map) # number of corners = number of sides
	return sum


def main():
	# map = read_file("test.txt")
	map = read_file("input.txt")

	print(compute_fencing_price(map))
	print(compute_bulk_fencing_price(map))


if __name__ == "__main__":
	main()
