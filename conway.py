from ctypes import cdll
gridLib = cdll.LoadLibrary('./libtick.so')

import argparse
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np

class grid(object):
    def __init__(self):
        self.obj = gridLib.grid_new()

    def randomPopulate(self, density):
        gridLib.grid_randomPopulate(self.obj, density)

    def tick(self):
        gridLib.grid_tick(self.obj)

    def save(self):
        gridLib.grid_save(self.obj)


if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--format", nargs=2, metavar=("width", "height"), help="specify width and height")
    parser.add_argument("--density", help="specify density of live cells in random seed")
    parser.add_argument("--seed", help="specify text file  or 'random' as seed")
    args = parser.parse_args()

    if args.format:
        WIDTH = int(args.format[0])
        HEIGHT = int(args.format[1])
    else:
        WIDTH = 1000
        HEIGHT = 1000
    if args.density:
        density = int(args.density)
    else:
        density = 10

    field = grid()
    if (not args.seed) or args.seed=="random":
        field.randomPopulate(density)
    # else:
    #     field = cycon.populate( args.seed )
    #     WIDTH, HEIGHT = field.shape

    field.save() # produces field.npy

    fig = plt.figure()
    im = plt.imshow( np.load("field.npy") , cmap='YlGn', vmin=0, vmax=1, interpolation="none")

    def init():
        im.set_data(np.zeros(( WIDTH, HEIGHT )))

    def animate(i):
        global field
        field.tick()
        field.save()
        im.set_data( np.load("field.npy") )
        return im

    anim = animation.FuncAnimation(fig, animate, init_func=init,
        frames=WIDTH*HEIGHT, interval=80)
    plt.show()
