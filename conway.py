import random

class grid:
    def __init__(self, x,y):
        self.width  = x
        self.height = y
        self.alive = [[]]

    def randomPopulate(self):
        for i in range(width):
            for j in range(height):
                alive[i][j] = random.uniform(0., 1.) < 0.5

    def countLiveNeighbours(self, i,j):
        liveNeighbours=0
        for di in range(-1,2):
            for dj in range(-1,2):
                if (not (di==0 and dj==0)):
                    try:
                        if alive[i+di][j+dj]:
                            liveNeighbours+=1
                    except IndexError:
                        pass
        return liveNeighbours

    def tick(self):
        updated = alive
        for i in range(width):
            for j in range(height):
                if alive[i][j]:
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
        alive = updated
