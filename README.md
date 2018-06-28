## Conway's Game of Life -- live renderer

Take a seed for Conway's Game of Life and watch it evolve live.
Written in Python using Cython

![live](life.gif)

### Usage
 - Random seed:
    `python conway.py --seed random`
 - Seed from file:
    `python conway.py --seed seeds/spaceship.txt`

See `python conway.py --help` for more.

Seeds from files must consist of a rectangular grid of 0s and 1s, seperated by spaces. You can create some using the scripts `seeds/createEmptySeed.py` and `seeds/createGeometricSeed.py`.

### Building
Requires `matplotlib`, `numpy` and `cython`
```
git clone https://github.com/davekch/conway.git
cd conway
python setup.py build_ext --inplace
```
