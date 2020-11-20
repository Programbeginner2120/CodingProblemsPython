def get_generation(cells, generations):
    row = len(cells)
    col = len(cells[0])
    numGens = 0
    neighborCells = 0
    newCells = [[0] * col] * row

    while (numGens < generations):
        for r in range(row):
            for c in range(col):
                if (r == 0):
                    if (c == 0):
                        neighborCells = cells[r][c + 1] + sum(cells[r + 1][c:c + 2])  # Upper left corner
                    elif (c == col - 1):
                        neighborCells = cells[r][c - 1] + sum(cells[r + 1][c - 1:c + 1])  # Upper right corner
                    else:
                        neighborCells = cells[r][c - 1] + cells[r][c + 1] + sum(
                            cells[r + 1][c - 1:c + 2])  # Top perimenter
                elif (r == row - 1):
                    if (c == 0):
                        neighborCells = cells[r][c + 1] + sum(cells[r - 1][c:c + 2])  # Lower left corner
                    elif (c == col - 1):
                        neighborCells = cells[r][c - 1] + sum(cells[r - 1][c - 1:c + 1])  # Lower right corner
                    else:
                        neighborCells = cells[r][c - 1] + cells[r][c + 1] + sum(
                            cells[r - 1][c - 1:c + 2])  # Bottom perimeter
                elif (0 < r < row - 1):
                    if (c == 0):
                        neighborCells = cells[r][c + 1] + sum(cells[r - 1][c:c + 2]) + sum(
                            cells[r + 1][c:c + 2])  # Left perimeter
                    elif (c == col - 1):
                        neighborCells = cells[r][c - 1] + sum(cells[r - 1][c - 1:c + 1]) + sum(
                            cells[r + 1][c - 1:c + 1])  # Right perimeter
                else:
                    neighborCells = cells[r][c - 1] + cells[r][c + 1] + sum(cells[r - 1][c - 1:c + 2]) + sum(
                        cells[r + 1][c - 1:c + 2])  # General case

                if (cells[r][c] == 1 and 2 < neighborCells < 3):
                    newCells[r][c] = 1
                if (cells[r][c] == 1 and neighborCells < 2):
                    newCells[r][c] = 0
                if (cells[r][c] == 1 and neighborCells > 3):
                    newCells[r][c] = 0
                if (cells[r][c] == 0 and neighborCells == 3):
                    newCells[r][c] = 1
        cells = newCells
        numGens += 1

    return newCells
