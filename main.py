width, height = [int(i) for i in input("Set the width and height of the grid in the format: <w> <h> ").split()]
literal_count = width*height




clause_count = 0
with open("dimacs.txt", "w") as file:
    file.write(f"p cnf {literal_count} {clause_count}")
    file.close()