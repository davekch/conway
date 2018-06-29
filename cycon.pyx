import random
import numpy as np
cimport numpy as np
cimport cython

def randomPopulate(width,height, density):
    alive = np.zeros((width,height), dtype=np.int32)
    for i in range(width):
        for j in range(height):
            alive[i,j] = 1 if random.uniform(0.,1.)<density else 0
    return alive

def populate(seed):
    alive = np.loadtxt(seed, dtype=np.int32)
    return alive

cdef int countLiveNeighbours(alive, int i, int j):
    cdef int liveNeighbours=0
    cdef int di
    cdef int dj
    for di in range(-1,2):
        for dj in range(-1,2):
            if not (di==0 and dj==0):
                try:
                    if alive[i+di, j+dj]==1:
                        liveNeighbours+=1
                except IndexError:
                    pass
    return liveNeighbours

# takes 2d-numpyarray and returns one
cpdef int[:,:] tick( alive, int width, int height ):
    updated = np.copy(alive)
    cdef int i
    cdef int j
    for i in range(width):
        for j in range(height):
            liveNeighbours = countLiveNeighbours(alive, i,j)
            if alive[i,j]==1:
                # if less than two live neighbours, cell dies
                # if more than 3 live neighbours, cell dies
                if liveNeighbours < 2 or liveNeighbours > 3:
                    updated[i,j] = 0
            else:
                # if 3 live neighbours, cell comes to life
                if liveNeighbours == 3:
                    updated[i,j] = 1
    return updated
