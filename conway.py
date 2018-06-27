import cycon
import argparse
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np

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

if (not args.seed) or args.seed=="random":
    field = cycon.randomPopulate(WIDTH, HEIGHT, density)
else:
    field = cycon.populate( args.seed )
    WIDTH, HEIGHT = field.shape

fig = plt.figure()
im = plt.imshow(field, cmap='YlGn', vmin=0, vmax=1, interpolation="none")

def init():
    im.set_data(np.zeros(( WIDTH, HEIGHT )))

def animate(i):
    global field
    field = cycon.tick(field)
    im.set_data(field)
    return im

anim = animation.FuncAnimation(fig, animate, init_func=init,
    frames=WIDTH*HEIGHT, interval=80)
plt.show()
