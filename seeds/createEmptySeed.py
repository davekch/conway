import sys

WIDTH, HEIGHT = int(sys.argv[1]), int(sys.argv[2])

with open("newEmptySeed.txt", "w") as f:
    for j in range(HEIGHT):
        for i in range(WIDTH):
            f.write("0 ")
        f.write("\n")
