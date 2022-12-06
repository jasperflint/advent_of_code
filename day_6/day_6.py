import os

script_dir = os.path.dirname(__file__)
day = "day_6_data"
# day = "day_6_test"
abs_path = os.path.join(script_dir, day)
print(abs_path)
raw_data = open(abs_path, "r")
data = str(list(raw_data)[0])


for i in range(0, len(data) - 3, 1):
    four_digit_check = []
    for s in range(0, 4):
        four_digit_check.append(data[i + s])

    if len(set(four_digit_check)) == len(four_digit_check):

        print(f"Result 1: {i+4}. All elements are unique.", four_digit_check)
        break

for i in range(0, len(data) - 14, 1):
    fourteen_digit_check = []
    for s in range(0, 14):
        fourteen_digit_check.append(data[i + s])

    if len(set(fourteen_digit_check)) == len(fourteen_digit_check):

        print(f"Result 2: {i+14}. All elements are unique.", fourteen_digit_check)
        break
