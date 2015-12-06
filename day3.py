input_file = open("input_day3.txt").read()
x_santa = y_santa = 0
x_robot = y_robot = 0

houses = {(0,0)}
robot_alive = True

for step in input_file:
    if robot_alive:
        if step == "^":
            y_santa += 1
        elif step == "v":
            y_santa -= 1
        elif step == ">":
            x_santa += 1
        else:
            x_santa -= 1
        houses.add((x_santa, y_santa))
    else:
        if step == "^":
            y_robot += 1
        elif step == "v":
            y_robot -= 1
        elif step == ">":
            x_robot += 1
        else:
            x_robot -= 1
        houses.add((x_robot, y_robot))

    robot_alive = not robot_alive

print len(set(houses))