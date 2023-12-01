
import re

def find_calibration_values(filename = '1_1_input.txt'):                      
    with open("input/" + filename) as file:
        result = 0
        for line in file:
            target_value = 0
            for char in line:
                if re.search("[0-9]", char):
                    target_value += 10*int(char)
                    break
            for char in line[::-1]:
                if re.search("[0-9]", char):
                    target_value += int(char)
                    break
            result += target_value
    return result


def find_calibration_values_with_str(filename = '1_1_input.txt'):
    digit_spelling = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }

    with open("input/" + filename) as file:
        result = 0
        for line in file:
            earliest_digit_position = 10**5
            latest_digit_position = -1
            earliest_digit = 0
            latest_digit = 0

            for digit in digit_spelling.keys():
                digit_str_matches = re.finditer(digit, line)
                for match in digit_str_matches:
                    digit_position = match.span()[0]
                    if digit_position < earliest_digit_position:
                        earliest_digit_position = digit_position
                        earliest_digit = digit_spelling[digit]
                    if digit_position > latest_digit_position:
                        latest_digit_position = digit_position
                        latest_digit = digit_spelling[digit]
            for i in range(len(line)):
                digit_int_found_start = re.search("[0-9]", line[i])
                if digit_int_found_start and i < earliest_digit_position:
                    earliest_digit_position = i
                    earliest_digit = int(line[i])
                    break
            for i in range(len(line)-1,-1,-1):
                digit_int_found_end = re.search("[0-9]", line[i])
                if digit_int_found_end and i > latest_digit_position:
                    latest_digit_position = i
                    latest_digit = int(line[i])
                    break
            value = 10*earliest_digit + latest_digit
            result += value
    return result

if __name__ == "__main__":
    # res = find_calibration_values("1_1_input.txt")
    # print(res)
    res = find_calibration_values_with_str("1_2_input.txt")
    print(res)
    # 51649 incorrect


