from ctypes import cdll
lib = cdll.LoadLibrary('./libfoo.so')
gridlib = cdll.LoadLibrary('./libtick.so')

class Foo(object):
    def __init__(self):
        self.obj = lib.Foo_new()

    def bar(self):
        lib.Foo_bar(self.obj)

    def get(self, i):
        return lib.Foo_get(self.obj, i)


class grid(object):
    def __init__(self):
        self.obj = gridlib.grid_new()

    def randomPopulate(self):
        gridlib.grid_randomPopulate(self.obj)

    def tick(self):
        gridlib.grid_tick(self.obj)

    def save(self):
        gridlib.grid_save(self.obj)


field = grid()
field.randomPopulate()
field.tick()
field.save()
