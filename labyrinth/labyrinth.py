NO = ["###", "###", "###"]  # No path
LR = ["###", "   ", "###"]  # Path from left to right
LT = ["# #", "  #", "###"]  # Path from left to top
BR = ["###", "#  ", "# #"]  # Path from bottom to right
LB = ["###", "  #", "# #"]  # Path from left to bottom
TR = ["# #", "#  ", "###"]  # Path from top to right


def render(array):
    for row in array:
        for i in range(3):
            for tile in row:
                print(tile[i], end="")
            print()


# ---------------- main ------------
if __name__ == '__main__':
    render([
        [NO, BR, LR, LB, NO],
        [LR, LT, NO, TR, LR]
    ])
