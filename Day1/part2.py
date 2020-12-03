numbers = []
# read the data from the file
with open('data.txt', 'r') as inp:
    numbers = inp.readlines()

target = 2020
status = False # we need this to determine when to break both loops
for i in range(0, len(numbers)):
    for j in range(i + 1, len(numbers)):
        remainder = target - (int(numbers[i].strip()) + int(numbers[j].strip()))
        if str(remainder)+"\n" in numbers:
            status = True
            print(int(numbers[i].strip()) * int(numbers[j].strip()) * remainder)
            break
    if status:
        break