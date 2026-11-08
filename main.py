width, height = [int(i) for i in input("Set the width and height of the grid in the format: <w> <h> ").split()]
literal_count = width*height

literal = 1
clauses = []

grid = [[1 + i + j*(width + 2) for i in range(width + 2)] for j in range(height + 2)] # + 2 for edges

print(grid)

#edges are always dead
for i in range(width + 2):
    clauses.append([-grid[0][i]])
    clauses.append([-grid[-1][i]])
    clauses.append([-grid[i][0]])
    clauses.append([-grid[i][-1]])

print(clauses)

with open("dimacs.cnf", "w") as file:
    file.write(f"p cnf {literal_count} {len(clauses)}\n")

    for clause in clauses:
        file.write(" ".join([str(n) for n in clause]) + " 0\n")


    file.close()