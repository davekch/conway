from ctypes import cdll
lib = cdll.LoadLibrary('./libfoo.so')

class Foo(object):
    def __init__(self):
        self.obj = lib.Foo_new()

    def bar(self):
        lib.Foo_bar(self.obj)

    def get(self, i):
        return lib.Foo_get(self.obj, i)


f = Foo()
f.bar()
print f.get(5);
