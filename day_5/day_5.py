import os
import copy

script_dir = os.path.dirname(__file__)
day = "day_5_data"
abs_path = os.path.join(script_dir, day)
print(abs_path)

raw_data = open(abs_path, "r")

data = []
for i in raw_data:
    i = str(i.strip())
    data.append(i)


boxes = [
    [],
    ["N", "D", "M", "Q", "B", "P", "Z"],
    ["C", "L", "Z", "Q", "M", "D", "H", "V"],
    ["Q", "H", "R", "D", "V", "F", "Z", "G"],
    ["H", "G", "D", "F", "N"],
    ["N", "F", "Q"],
    ["D", "Q", "V", "Z", "F", "B", "T"],
    ["Q", "M", "T", "Z", "D", "V", "S", "H"],
    ["M", "G", "F", "P", "N", "Q"],
    ["B", "W", "R", "M"],
]
boxes_1 = copy.deepcopy(boxes)
boxes_2 = copy.deepcopy(boxes)

#################################################
#                 --- Part 1 ---                #
#################################################

result_1 = ""
print("\nBoxes at Start")
for i in range(1, 9):
    print(boxes_1[i])

for i in data:
    a = i.split(" ")
    num_to_move = int(a[1])
    move_from = int(a[3])
    move_to = int(a[5])
    for i in range(1, num_to_move + 1, 1):
        item = boxes_1[move_from][-1]
        boxes_1[move_from].pop()
        boxes_1[move_to].append(item)

print("\nBoxes at End")
for i in range(1, 10):
    try:
        res = boxes_1[i][-1]
    except:
        res = " "
    result_1 += res
    print(boxes_1[i])

print("Result 1: ", result_1)


#################################################
#                 --- Part 2 ---                #
#################################################

result_2 = ""
for i in data:
    a = i.split(" ")
    num_to_move = int(a[1])
    move_from = int(a[3])
    move_to = int(a[5])
    temp_list = []
    for i in range(1, num_to_move + 1, 1):
        item = boxes_2[move_from][-1]
        boxes_2[move_from].pop()
        temp_list.insert(0, item)

    boxes_2[move_to].extend(temp_list)
    
print("\nBoxes at End")
for i in range(1, 10):
    try:
        res = boxes_2[i][-1]
    except:
        res = ""
    result_2 += res
    print(boxes_2[i])


print("Result 2: ", result_2)
