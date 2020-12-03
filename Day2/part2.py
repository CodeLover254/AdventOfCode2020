with open('data.txt', 'r') as inp:
    passwords = inp.readlines()

# part 2
valid = 0
for password in passwords:
    # extract the information from the string
    sections = password.strip().split(" ")
    pos1, pos2 = tuple(sections[0].split("-"))
    target_letter = sections[1].replace(":", "").strip()
    given_password = sections[2].strip()
    # if a letter appears in both positions then that's a no
    if given_password[int(pos1) - 1] == target_letter and given_password[int(pos2) - 1] == target_letter:
        # invalid just continue
        continue
    # if it appears in either position then it  is valid.
    if given_password[int(pos1) - 1] == target_letter or given_password[int(pos2) - 1] == target_letter:
        valid += 1

print(valid)