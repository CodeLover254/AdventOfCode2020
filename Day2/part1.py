with open('data.txt', 'r') as inp:
    passwords = inp.readlines()

# part 1
valid = 0
for password in passwords:
    # we need to extract the information from the line of text that is in the format
    # min-max target: password
    sections = password.strip().split(" ")
    minimum, maximum = tuple(sections[0].split("-"))
    target_letter = sections[1].replace(":", "").strip()
    given_password = sections[2].strip()
    occurrences = 0
    # thinking of a faster way to count the occurrence of a character in a string?
    for char in given_password:
        if target_letter == char:
            occurrences += 1

    if int(minimum) <= occurrences <= int(maximum):
        valid += 1

print(valid)
