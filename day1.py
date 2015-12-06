directions = open("input_day1.txt").read()
# directions = input_file.read()


# Each '(' means Santa goes up a floor
# Each ')' means Santa goes down a floor
# Find the final floor Santa stops at
up_floors = directions.count("(")
down_floors = directions.count(")")
final_floor = up_floors - down_floors

print "Final Floor: " + str(final_floor)


# Find the position of the character that causes Santa to enter the basement
# The basement is located at floor == -1
current_floor = 0
position = 0

for char in directions:
    if char == '(':
        current_floor += 1
    else:
        current_floor -= 1
    position += 1

    if current_floor == -1:
        break

print "Position to enter basement: " + str(position)