import difflib
import os

script_dir = os.path.dirname(__file__)
day = "day_3_data"
abs_path = os.path.join(script_dir, day)
print(abs_path)

raw_data = open(abs_path, "r")
data = []
total = 0
total_2 = 0

for i in raw_data:
    i = str(i.strip())
    data.append(i)

alpha_dict = {}

alphabet_list = list(map(chr, range(ord("a"), ord("z") + 1)))
alphabet_list.extend(list(map(chr, range(ord("A"), ord("Z") + 1))))

# print(alphabet_list)
index = 1
for i in alphabet_list:
    alpha_dict[i] = index
    index += 1
# print(alpha_dict)


# print(data[0])
j = [[]]
for i in data:
    length = int(len(i) / 2)
    # print(length)
    # print(i[0:length], i[length : len(i)])
    k = list(difflib.Differ().compare(i[0:length], i[length : len(i)]))
    # print((k))
    for i in list(k):
        if i[0] == " ":
            # print("yes: ", i[2])
            total += alpha_dict[f"{i[2]}"]
            break

print("Total Part 1: ", total)
"""
print(data[0])
l = []

s = "gtZDjBcmpcDgpZcmmbgtdtqmCGVCGGsvhCFCCqvmCMMM"
t = "JrhfzfLTNfJhPnhQnfzHfCFFQFSGvMFCGQFsQSMSVs"
u = "TllTRrfNNlfzwhtZBZgtRDBp"
print(list(s.strip()))
y = list(set(list(s.strip())).intersection(list(t.strip())))

print(y)

z = list(set(list(u.strip())).intersection(y))
print(z)
"""

for i in range(3, len(data) + 3, 3):
    a = str(data[i - 3])
    b = str(data[i - 2])
    c = str(data[i - 1])
    # print(c)
    d = list(a.strip())
    e = list(b.strip())
    f = list(c.strip())

    g = list(set(d).intersection(e))
    h = list(set(g).intersection(f))
    # print(h)
    for i in list(h):
        # print(alpha_dict[f"{i}"])
        total_2 += alpha_dict[f"{i}"]
        break

print("Total Part 2: ", total_2)
