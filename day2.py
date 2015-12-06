input_data = open("input_day2.txt").read().splitlines()
# input_data = input_file.read()

total_feet_present = 0
total_feet_ribbon = 0


def surface_area(l, w, h):
    return 2*l*w + 2*w*h + 2*h*l


def smallest_side(l, w, h):
    return min(l*w, w*h, h*l)


def shortest_perimeter(l, w, h):
    dimension = [l, w, h]
    dimension.remove(max(dimension))
    perimeter = 0
    for num in dimension:
        perimeter += 2 * num
    return perimeter


for dimension in input_data:
    # dimension = dimension.split("x")
    # Convert the dimensions from string to int to allow calculations
    dimension = map(int, dimension.split("x"))
    length, width, height = dimension

    # Slack is size of the smallest side, which is added to the feet_required
    slack = smallest_side(length, width, height)
    feet_required = surface_area(length, width, height) + slack
    total_feet_present += feet_required

    print dimension, length, width, height, slack, feet_required
    # print dimension.strip("\n").split("x")

    # Day 2, Part 2
    ribbon_length = shortest_perimeter(length, width, height)
    bow_length = 1
    for num in dimension:
        bow_length *= num
    total_feet_ribbon += ribbon_length + bow_length

    print ribbon_length, bow_length

print "Total square feet required for present: " + str(total_feet_present)
print "Total feet requited for ribbon: " + str(total_feet_ribbon)