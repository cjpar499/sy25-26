fname = "output.txt"
file= open(fname, "w")
for i in range(100):
    file.write(f"This is line {i} .\n")
file.close()
