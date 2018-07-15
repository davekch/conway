## Conway's Game of Life &mdash; live renderer

Take a seed for Conway's Game of Life and watch it evolve live.
Written in C++ and Python using ctypes

![live](life.gif)

### Usage
 - Random seed:
    `python conway.py --seed random`
 - Seed from file:
    `python conway.py --seed seeds/spaceship.txt`

See `python conway.py --help` for more.

Seeds from files must consist of a rectangular grid of 0s and 1s, seperated by spaces. You can create some using the scripts `seeds/createEmptySeed.py` and `seeds/createGeometricSeed.py`.

### Requirements
**Python**
 - `matplotlib` and `numpy`

**C++**
 - I use [Carl Roger](https://github.com/rogersce)'s amazing library [cnpy](https://github.com/rogersce/cnpy) to save and load numpy-arrays in C++. In the next section I assume that it is installed in `/usr/local/lib`.


 ### Building
```
git clone https://github.com/davekch/conway.git
cd conway

g++ -c -fPIC tick.cpp -o tick.o --std=c++11
g++ -shared -Wl,-soname,libtick.so -o libtick.so tick.o -L/usr/local/lib -lcnpy -lz
```

--------
The branch `cython` contains older code using a different approach and doesn't depend on `cnpy`.
