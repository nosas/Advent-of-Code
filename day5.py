input_file = "input_day5.txt"
vowels = 'aeiuo'
bad_strings = ["ab", "cd", "pq", "xy"]


def check_bad_string(word):
    for case in bad_strings:
        if case in word:
            return False
    return True


def count_vowels(word):
    sum = 0

    for char in word:
        if char in vowels:
            sum += 1

    return sum >= 3


def check_double_letter(word):
    double_letter = [letter + letter for letter in list(set(word))]
    for case in double_letter:
        if case in word:
            return True
    return False


def check_input(word):
    result = check_bad_string(word), count_vowels(word), check_double_letter(word)
    if result == (True, True, True):
        return True
    return False


with open(input_file) as f:
    sum_good_string = 0
    for word in f.readlines():
        if check_input(word):
            sum_good_string += 1

print sum_good_string

