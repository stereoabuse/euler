################################################################################
#                          Project Euler Problem 011                           #
#                     https://projecteuler.net/problem=011                     #
#                                                                              #
# Author:   Chris B.                                                           #
# Date:     November 05, 2020                                                  #
################################################################################

def prob_011():
    "return greated product of 4 adjactent numbers on the grid"
    grid = open('utility/euler_011_grid.txt').readlines()

    list_grid = []     
    for line in grid:
        line_grid = []
        line = line.split()
        for item in line:
            line_grid.append(int(item))
        list_grid.append(line_grid)
    down_list, across_list = [], []
    diagonal_down_list, diagonal_up_list = [], []
    
    for index in range(17):
        for subindex in range(17):
            # across
            across = list_grid[index][subindex] * \
                     list_grid[index][subindex+1]* \
                     list_grid[index][subindex+2] * \
                     list_grid[index][subindex+3]
            across_list.append(across)

            # down
            down = list_grid[index][subindex] * \
                   list_grid[index+1][subindex]* \
                   list_grid[index+2][subindex] * \
                   list_grid[index+3][subindex]
            down_list.append(down)

            # diagonal down
            diagonal_down = list_grid[index][subindex] *\
                            list_grid[index+1][subindex+1]* \
                            list_grid[index+2][subindex+2] * \
                            list_grid[index+3][subindex+3]
            diagonal_down_list.append(diagonal_down)

            #diagonal up
            try:
                diagonal_up = list_grid[index][subindex] * \
                              list_grid[index-1][subindex+1]* \
                              list_grid[index-2][subindex+2] * \
                              list_grid[index-3][subindex+3]
                diagonal_up_list.append(diagonal_up)
            except IndexError:
                pass
    return sorted(down_list + across_list + diagonal_down_list + diagonal_up_list, reverse = True)[0]

prob_011()