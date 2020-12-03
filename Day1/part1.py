numbers = []
# read the data from the file
with open('data.txt', 'r') as inp:
    numbers = inp.readlines()

target = 2020
# linear solution.
for i in range(0, len(numbers)):
    # calculate the remainder and check if it is in the list of numbers.
    remainder = target - int(numbers[i].strip())
    if str(remainder)+"\n" in numbers:
        status = True
        print(int(numbers[i].strip()) * remainder)
        break
