# print method optimized for tables
def print_matrice(m, m_size):
    for i in range(m_size):
        print("")
        for j in range(m_size):
            print(m[i][j], end=" \t")


# initializes an empty matrice on given size with all cells at a given initial value
def initialize_matrice(matrice_size, initial_value):

    matrice = []

    # gives second dimension to each row
    for i in range(matrice_size):
        matrice.append([])

    # actually initializes matrice to values
    for i in range(matrice_size):
        for j in range(matrice_size):
            matrice[i].append(initial_value)

    return matrice


def spiral_fill(table):

    # dictionary of matrice boundaries
    borders = {
        "north": 0,
        "south": 0,
        "east": 0,
        "west": 0
    }

    # dictionary of filled boundaries
    filled = {
        "north": 0,
        "south": 0,
        "east": 0,
        "west": 0
    }

    matrice_size = len(table)
    matrice_border = matrice_size -1

    borders["north"] = 0
    borders["south"] = matrice_border
    borders["east"] = matrice_border
    borders["west"] = 0

    num = 1

    while num <= matrice_size**2:

        # fills north -- west to east
        for j in range(borders["west"] + filled["west"], borders["east"] - filled["east"] + 1):
            table[filled["north"]][j] = num
            num += 1

        filled["north"] += 1

        # fills east -- north to south
        for i in range(borders["north"] + filled["north"], borders["south"] - filled["south"] + 1):
            table[i][borders["east"] - filled["east"]] = num
            num += 1

        filled["east"] += 1

        # fills south -- east to west
        for j in range(borders["east"] - filled["east"], borders["west"] + filled["west"] - 1, - 1):
            table[borders["south"] - filled["south"]][j] = num
            num += 1

        filled["south"] += 1

        # fills west -- south to north
        for i in range(borders["south"] - filled["south"], borders["north"] + filled["north"] - 1, - 1):
            table[i][borders["west"] + filled["west"]] = num
            num += 1

        filled["west"] += 1


def main():
    dimension = int(input("enter matrice size: "))
    print("initializing matrice...")
    mat = initialize_matrice(dimension, 0)
    spiral_fill(mat)
    print("process done!")
    print_matrice(mat, len(mat))

main()