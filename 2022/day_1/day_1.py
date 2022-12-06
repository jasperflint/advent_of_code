import os

script_dir = os.path.dirname(__file__)
day = "day_1_data"
abs_path = os.path.join(script_dir, day)
print(abs_path)

data = open(abs_path, "r")

j = [0]
index = 0
for i in data:
    #print("index: ", index)
    # print("j", j)
    try:
        i = int(i.strip())
    except ValueError:
        i
    

    if isinstance(i, int): 
        j[index] += i
        # print(j[index])
    else:
        index += 1
        j.append(0)

print("Part 1: ", max(j))

j.sort(reverse=True)

print("Part 2: ", sum(j[0:3]))