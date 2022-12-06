raw_data = open("day_4_data", "r")
data = []
total = 0
total_2 = 0

for i in raw_data:
    i = str(i.strip())
    data.append(i)

# print(data)

for i in data:
    a = i.split(",")
    # print(a)
    b = a[0].split("-")
    c = list(range(int(b[0]), int(b[1]) + 1, 1))
    # print(c)
    d = a[1].split("-")
    e = list(range(int(d[0]), int(d[1]) + 1, 1))
    # print(e)
    f = set(c).issubset(e)
    g = set(c).issuperset(e)
    # print(f)
    # print(g)
    if f or g is True:
        # print("one is true")
        total += 1
        # print(total)

print("total 1: ", total)

for i in data:
    a = i.split(",")
    # print(a)
    b = a[0].split("-")
    c = list(range(int(b[0]), int(b[1]) + 1, 1))
    # print(c)
    d = a[1].split("-")
    e = list(range(int(d[0]), int(d[1]) + 1, 1))
    # print(e)
    f = list(set(c).intersection(e))
    # print(f)
    # print(bool(f))
    if bool(f):
        total_2 += 1
        # print(total_2)

print("total 2: ", total_2)
