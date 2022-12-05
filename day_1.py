
data = open("day_1_data", "r")

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

print(max(j))

j.sort(reverse=True)

print(j[0:3])

print(sum(j[0:3]))