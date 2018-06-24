import random
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

class grid:
    def __init__(self, x,y):
        self.width  = x
        self.height = y
        self.alive = np.zeros((x,y))

    def randomPopulate(self, density):
        for i in range(self.width):
            for j in range(self.height):
                self.alive[i,j] = 1 if random.uniform(0.,1.)<density else 0

    def countLiveNeighbours(self, i,j):
        liveNeighbours=0
        for di in range(-1,2):
            for dj in range(-1,2):
                if not (di==0 and dj==0):
                    try:
                        if self.alive[i+di, j+dj]:
                            liveNeighbours+=1
                    except IndexError:
                        pass
        return liveNeighbours

    def tick(self):
        updated = self.alive
        for i in range(self.width):
            for j in range(self.height):
                if self.alive[i][j]:
                    # if less than two live neighbours, cell dies
                    if self.countLiveNeighbours(i,j) < 2:
                        updated[i][j] = False
                    # if more than 3 live neighbours, cell dies
                    elif self.countLiveNeighbours(i,j) > 3:
                        updated[i][j] = False
                else:
                    # if 3 live neighbours, cell comes to live
                    if self.countLiveNeighbours(i,j) == 3:
                        updated[i][j] = True
        self.alive = updated

if __name__=="__main__":

    fig = plt.figure()
    plt.axis()
    ax = plt.gca()
    #ax.set_aspect(1)

    field = grid(50,50)
    field.randomPopulate(0.5)

    for i in range(field.width):
        for j in range(field.height):
            pixel=plt.Rectangle( (i*10,j*10), 10,10 )
            ax.add_patch(pixel)

    def init():
        return []

    def animate(i):
        field.tick()
        patches = []
        for i in range(field.width):
            for j in range(field.height):
                if field.alive[i][j]:
                    color = "b"
                else:
                    color = "w"
                pixel = plt.Rectangle( (i*10,j*10), 10,10, fc=color )
                patches.append(ax.add_patch(pixel))
        return patches

    plt.axis("scaled")
    anim = animation.FuncAnimation( fig, animate, init_func=init, frames=30, interval=1, blit=True )
    plt.show()
