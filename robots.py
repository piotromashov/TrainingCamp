robots = 3

total_time = 10

max_building = 0

for robot_level in xrange(0,10):
	robots_builded[robot_level-1] = robot_level*total_time

	if max_building < robots_builded:
		max_building = robots_builded

		