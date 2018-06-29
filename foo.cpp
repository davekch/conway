#include <iostream>

class Foo{
    public:
        void bar(){
            std::cout << "Hello" << std::endl;
        }
        int get(int i){
            return i;
        }
};

extern "C" {
    Foo* Foo_new(){ return new Foo(); }
    void Foo_bar(Foo* foo){ foo->bar(); }
    int Foo_get(Foo* foo, int i){ return foo->get(i); }
}
