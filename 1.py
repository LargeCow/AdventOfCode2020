
# question 1
with open('inputs/input_1.txt', 'r') as input_file:
    lines = input_file.readlines()
    for i in lines:
        for x in lines:
                x, i = int(x), int(i)
                res = x +i
                if res == 2020:
                    print(x * i)

input_file.close()

# question 2
with open('inputs/input_1.txt', 'r') as input_file:
    lines = input_file.readlines()
    for i in lines:
        for x in lines:
            for y in lines:
                x, i, y = int(x), int(i), int(y)
                res = x + i + y
                if res == 2020:
                    print(x * i * y)
                    break
input_file.close()