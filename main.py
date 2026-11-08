import itertools


width, height = 3,3 #[int(i) for i in input("Set the width and height of the grid in the format: <w> <h> ").split()]
literal_count = width*height

literal = 1
clauses = []

grid = [[1 + i + j*(width + 2) for i in range(width + 2)] for j in range(height + 2)] # + 2 for edges

#edges are always dead
for i in range(width + 2):
    clauses.append([-grid[0][i]])
    clauses.append([-grid[-1][i]])
    clauses.append([-grid[i][0]])
    clauses.append([-grid[i][-1]])


directions = []
for i in range(-1, 2):
    for j in range(-1, 2):
        if i == 0 and j == 0:
            continue
        directions.append([i, j])

for y in range(1, height + 1):
    for x in range(1, width + 1):
        current = grid[y][x]
        around = []
        for dir in directions:
            around.append(grid[y + dir[0]][x + dir[1]])

        # if current -> at least two around are alive (i take all 7-tuples and all of them have to have at least one alive)
        combs = itertools.combinations(around, len(around) - 1)
        for comb in combs:
            clauses.append(list(comb) + [-current])

        # if current -> no more than 3 around are alive = at least 5 around are false (i take all 3-tuples and all of them have to nave at least one dead)
        combs = itertools.combinations(around, len(around) - 4)
        for comb in combs:
            clauses.append([-n for n in comb] + [-current])


with open("file.cnf", "w") as file:
    file.write(f"p cnf {literal_count} {len(clauses)}\n")

    for clause in clauses:
        file.write(" ".join([str(n) for n in clause]) + " 0\n")


    file.close()