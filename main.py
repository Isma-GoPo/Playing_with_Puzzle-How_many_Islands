# functions
def is_in_map(i, j, grid) -> bool:
    """Returns True if i,j are valid index for grid (are inside the map)"""
    if (0 <= i < len(grid) and 
        0 <= j < len(grid[0]) ):
        return True
    else:
        return False

def is_land(i, j, grid) -> bool:
    """Returns True if is land, False if is water or outside the map"""
    if not is_in_map(i, j, grid):
        return False
    if grid[i][j] == "1":
        return True # If it is "1" it is land
    else:
        return False # If it is "0" it is water

def delete_land_and_adjacent(i, j, grid) -> None:
    """Turns the land and its adjacent lands to water recursively"""
    if not is_land(i, j, grid):
        return
    
    grid[i][j] = "0" # This land is checked, not to be checked again
    
    # Delete adyacent lands
    delete_land_and_adjacent(i-1, j, grid)
    delete_land_and_adjacent(i+1, j, grid)
    delete_land_and_adjacent(i, j-1, grid)
    delete_land_and_adjacent(i, j+1, grid)

# main
def count_islands(grid: list[list[str]]) -> int:
    """main function, returns the number of islands (disconnections of horizontal/vertically adjacent lands)"""
    number_of_islands = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if is_land(i,j, grid):
                delete_land_and_adjacent(i,j, grid) 
                number_of_islands += 1

    return number_of_islands

# Running the file
if __name__ == "__main__":
    import examples
    examples_dict = {k:v for k,v in vars(examples).items() if k[:2] != "__"}
    for example_name, example_grid in examples_dict.items():
        number_of_islands = count_islands(example_grid)
        print(f"INPUT: {example_name}")
        print(f"OUTPUT: {number_of_islands}\n")
