import random
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import argparse

class grid:
    def __init__(self, x,y):
        self.width  = x
        self.height = y
        self.alive = np.zeros((x,y))

    def randomPopulate(self, density):
        for i in range(self.width):
            for j in range(self.height):
                self.alive[i,j] = 1 if random.uniform(0.,1.)<density else 0

    def populate(self, seed):
        self.alive = np.loadtxt(seed, dtype=np.int)
        self.width, self.height = self.alive.shape

    def countLiveNeighbours(self, i,j):
        liveNeighbours=0
        for di in range(-1,2):
            for dj in range(-1,2):
                if not (di==0 and dj==0):
                    try:
                        if self.alive[i+di, j+dj]==1:
                            liveNeighbours+=1
                    except IndexError:
                        pass
        return liveNeighbours

    def tick(self):
        updated = self.alive
        for i in range(self.width):
            for j in range(self.height):
                if self.alive[i,j]==1:
                    # if less than two live neighbours, cell dies
                    if self.countLiveNeighbours(i,j) < 2:
                        updated[i,j] = 0
                    # if more than 3 live neighbours, cell dies
                    elif self.countLiveNeighbours(i,j) > 3:
                        updated[i,j] = 0
                else:
                    # if 3 live neighbours, cell comes to life
                    if self.countLiveNeighbours(i,j) == 3:
                        updated[i,j] = 1
        self.alive = updated


parser = argparse.ArgumentParser()
parser.add_argument("--format", nargs=2, metavar=("width", "height"), help="specify width and height")
parser.add_argument("--density", help="specify density of live cells in random seed")
parser.add_argument("--seed", help="specify text file  or 'random' as seed")
args = parser.parse_args()

if args.format:
    WIDTH = int(args.format[0])
    HEIGHT = int(args.format[1])
else:
    WIDTH = 70
    HEIGHT = 70
if args.density:
    density = float(args.density)
else:
    density = 0.1

field = grid(WIDTH, HEIGHT)
if (not args.seed) or args.seed=="random":
    field.randomPopulate(density)
else:
    field.populate( args.seed )
    WIDTH = field.width
    HEIGHT = field.height

fig = plt.figure()
data = field.alive
im = plt.imshow(data, cmap='YlGn', vmin=0, vmax=1)

def init():
    im.set_data(np.zeros(( WIDTH, HEIGHT )))

def animate(i):
    field.tick()
    data = field.alive
    im.set_data(data)
    return im

anim = animation.FuncAnimation(fig, animate, init_func=init,
    frames=WIDTH*HEIGHT, interval=50)
plt.show()
