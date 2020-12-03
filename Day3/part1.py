with open('data.txt', 'r') as inp:
    rows = inp.readlines()

# we need to move 3 right 1 down up o the bottom most row
trees = 0
right_by = 3
for i in range(1, len(rows)):
    if rows[i][right_by] == "#":
        # aaah we found a tree!
        trees += 1

    right_by += 3  # we move right by 3. Our downward movement is already taken care of

    # the forest extends to the right as much as it extends downwards so we need
    # to take care when our right_by reaches beyond the length of the row and do the necessary adjustments
    if right_by >= len(rows[i].strip()):
        right_by = right_by - len(rows[i].strip())

print(trees)
