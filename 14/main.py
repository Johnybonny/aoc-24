def read_file(filename):
	robots = []
	with open(filename, "r") as file:
		for line in file:
			robot = {}
			position = line.split(" ")[0].split("=")[1].split(",")
			robot["position"] = [int(position[0]), int(position[1])]
			velocity = line.split(" ")[1].split("=")[1].split(",")
			robot["velocity"] = [int(velocity[0]), int(velocity[1])]
			robots.append(robot)
	return robots


def get_robot_final_position(robot, width, length, time):
	final_position = []
	final_position.append((robot["position"][0] + robot["velocity"][0] * time) % width)
	final_position.append((robot["position"][1] + robot["velocity"][1] * time) % length)
	return final_position


def update_quadrants(quadrants, quadrants_borders, final_position):
	if final_position[0] < quadrants_borders[0] and final_position[1] < quadrants_borders[1]:
		quadrants[0] += 1
	elif final_position[0] < quadrants_borders[0] and final_position[1] > quadrants_borders[1]:
		quadrants[2] += 1
	elif final_position[0] > quadrants_borders[0] and final_position[1] < quadrants_borders[1]:
		quadrants[1] += 1
	elif final_position[0] > quadrants_borders[0] and final_position[1] > quadrants_borders[1]:
		quadrants[3] += 1


def get_safety_factor(robots, width, length, time_elapsed):
	quadrants = [0] * 4
	for robot in robots:
		final_position = get_robot_final_position(robot, width, length, time_elapsed)
		quadrants_borders = [width // 2, length // 2]
		update_quadrants(quadrants, quadrants_borders, final_position)


	safety_factor = quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]
	return safety_factor


def update_robot_position(robot, width, length):
	robot["position"][0] = (robot["position"][0] + robot["velocity"][0]) % width
	robot["position"][1] = (robot["position"][1] + robot["velocity"][1]) % length


def print_robots_nicely(robots, width, length, file):
	taken_positions = [[False] * width for _ in range(length)]
	for robot in robots:
		taken_positions[robot["position"][1]][robot["position"][0]] = True

	for i in range(len(taken_positions)):
		for j in range(len(taken_positions[0])):
			if taken_positions[i][j]:
				file.write("*")
			else:
				file.write(" ")
		file.write("\n")


def look_for_christmas_tree(robots, width, length, max_time):
	with open("../bin/trees.txt", "w") as file:
		time_elapsed = 0
		while time_elapsed < max_time:
			time_elapsed += 1
			for robot in robots:
				update_robot_position(robot, width, length)

			file.write(f"Time elapsed: {time_elapsed}\n")
			print_robots_nicely(robots, width, length, file)
			file.write("-" * width + "\n")


def main():
	# robots = read_file("test.txt")
	# print(get_safety_factor(robots, 11, 7, 100))
	# look_for_christmas_tree(robots, 11, 7, 100)

	robots = read_file("input.txt")
	print(get_safety_factor(robots, 101, 103, 100))
	look_for_christmas_tree(robots, 101, 103, 10000)



if __name__ == "__main__":
	main()
