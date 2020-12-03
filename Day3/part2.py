with open('data.txt', 'r') as inp:
    rows = inp.readlines()

# slopes in the format right,down
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]


# we need to define a function to do the math for us. not a must but I feel it's cleaner
def get_trees(right_by, down_by):
    trees = 0
    right = right_by
    for i in range(down_by, len(rows), down_by):  # . Our downward movement is already taken care of using step
        if rows[i][right] == "#":
            # aaah we found a tree!
            trees += 1

        right += right_by  # we move right by right which is the initial value we received

        # the forest extends to the right as much as it extends downwards so we need
        # to take care when our right_by reaches beyond the length of the row and do the necessary adjustments
        if right >= len(rows[i].strip()):
            right -= len(rows[i].strip())

    return trees


result = 1
for slope in slopes:
    result *= get_trees(slope[0], slope[1])

print(result)
