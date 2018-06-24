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
                    # if 3 live neighbours, cell comes to live
                    if self.countLiveNeighbours(i,j) == 3:
                        updated[i,j] = 1
        self.alive = updated

if __name__=="__main__":

    field = grid(50,50)
    field.randomPopulate(0.05)

    fig = plt.figure()
    data = field.alive
    im = plt.imshow(data, cmap='gist_gray_r', vmin=0, vmax=1)

    def init():
        im.set_data(np.zeros((50, 50)))

    def animate(i):
        field.tick()
        data = field.alive
        im.set_data(data)
        return im

    anim = animation.FuncAnimation(fig, animate, init_func=init, frames=50 * 50,
                                   interval=50)
    plt.show()
