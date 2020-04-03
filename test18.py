# 2D lists
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[0][0]) # 1st row and 1st element in the list at that row
print(number_grid[3][0]) # Last row and 1st element



# Nested for loop
for row in number_grid:
    print(row)

# Accessing each element
for row in number_grid:
    for col in row:
        print(col)