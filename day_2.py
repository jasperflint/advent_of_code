data1 = open("day_2_data", "r")
data2 = open("day_2_data", "r")

def round_1(data1):
    print("round 1!")
    # print(len(list(data)))
    total = 0
    legend = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}
    for i in data1:
        i = i.strip()
        # print(i)
        i.split(" ")
        # print("opponent: ", i[0], "me: ", i[2])

        # print(legend[i[0]])

        if legend[i[0]] == 2 and legend[i[2]] == 3:  # my scissors beats their paper
            total += 9
        elif legend[i[0]] == 1 and legend[i[2]] == 2:  # my paper beats their rock
            total += 8
        elif legend[i[0]] == 3 and legend[i[2]] == 1:  # my rock beats their scissors
            total += 7
        elif legend[i[2]] == legend[i[0]]:
            # print(i)
            num = legend[i[0]]
            # print(num)
            total += num + 3
        else:
            num = legend[i[2]]
            total += num
        
    return total


def round_2(data2):
    print("round 2!")
    # print(len(list(data)))
    total = 0
    legend = {"A": 1, "B": 2, "C": 3, "X": "lose", "Y": "draw", "Z": "win"}
    for i in data2:
        i = i.strip()
        # print(i)
        i.split(" ")
        # print("opponent: ", i[0], "me: ", i[2])

        # print(legend[i[0]])

        if legend[i[2]] == "win":  # win
            if legend[i[0]] == 1:
                total += 8
            elif legend[i[0]] == 2:
                total += 9
            elif legend[i[0]] == 3:
                total += 7
        elif legend[i[2]] == "draw":  # draw
            num = legend[i[0]]
            total += num + 3
        elif legend[i[2]] == "lose":  # lose
            if legend[i[0]] == 1:
                total += 3
            elif legend[i[0]] == 2:
                total += 1
            elif legend[i[0]] == 3:
                total += 2
        else:
            print("error")
    return total


print(round_1(data1))
print(round_2(data2))


# print("opponent: ", i[0], "me: ", i[2])
