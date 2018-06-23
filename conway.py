import random
from matplotlib import pyplot as plt

class grid:
    def __init__(self, x,y):
        self.width  = x
        self.height = y
        self.alive = []

    def randomPopulate(self, density):
        for i in range(self.width):
            self.alive.append( [ random.uniform(0.,1.)<density for i in range(self.height) ] )

    def countLiveNeighbours(self, i,j):
        liveNeighbours=0
        for di in range(-1,2):
            for dj in range(-1,2):
                if (not (di==0 and dj==0)):
                    try:
                        if self.alive[i+di][j+dj]:
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

    plt.axes()
    field = grid(50,50)
    field.randomPopulate(0.5)

    for i in range(field.width):
        for j in range(field.height):
            if field.alive[i][j]:
                color = "b"
            else:
                color = "w"
            pixel = plt.Rectangle( (i*10,j*10), 10,10, fc=color )
            plt.gca().add_patch(pixel)

    plt.axis("scaled")
    plt.show()
