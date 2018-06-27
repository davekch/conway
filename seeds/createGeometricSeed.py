import sys

WIDTH, HEIGHT = int(sys.argv[1]), int(sys.argv[2])

with open("geometric.txt", "w") as f:
    for j in range(HEIGHT):
        for i in range(WIDTH):
            if i%4==0 or j%5==0:
                f.write("1 ")
            else:
                f.write("0 ")
        f.write("\n")
