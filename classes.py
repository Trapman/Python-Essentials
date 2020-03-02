# CLASSES ####################

class Bulldog:
    sound = "woof! I'm hungry!!"
    movement = 'walks like a bully.'
    
    def woof(self):        # first parameter is always self, but you can name it whatever you want
        print(self.sound)  # self is a reference to the object (not the class)
        
    def move(self):
        print(self.movement)
        
def main():
    buford = Bulldog()
    buford.woof
    buford.move
    
if __name__ == '__main__': main()

# CONSTRUCTING AN OBJECT ###################
# an object is an instance of a class
# __init__ is the constructor
class Animal:
    def __init__(self, type, name, sound):  # 'initializer' or constructor. always self, followed by whatever object variables you want to include
        self._type = type
        self._name = name
        self._sound = sound
        
    def type(self):
        return sel f._type
    
    def name(self):
        return self._name
    
    def sound(self):
        return self._sound
    
def print_animal(o):
    if not isinstance(o, Animal):
        raise TypeError('print_animal(): requires an Animal')
    print('The {} is named "{}" and says "{}".'.format(o.type(), o.name(), o.sound()))

def main():
    a0 = Animal('kitten', 'hally', 'rawr')
    a1 = Animal('duck', 'donald', 'quack')
    print_animal(a0)
    print_animal(a1)
    print_animal(Animal('velociraptor', 'veronica', 'hello'))
    
if __name__ = '__main__': main()

# ITERATOR OBJECTS #####################
# class that provides a sequence of items
# 
class inclusive_range:
    def __init__(self, *args):    # constructor
        numargs = len(args)
        self._start = 0
        self._step = 1
        
        if numargs < 1:
            raise TypeError(f'expected at least 1 argument, but got {numargs}')
        elif numargs == 1:
            self._stop = args[0]
        elif numargs == 2:
            (self._start, self._stop) = args
        elif numargs == 3:
            (self._start, self._stop, self.step) = args
        else:
            raise TypeError(f'expected at most 3 arguments, but got {numargs}')
        
        self._next = self._start
        
    def __iter__(self):  # special iterator method
        return self
    
    def __next__(self):
        if self._next > self._stop:
            raise StopIteration
        else:
            _r = self._next
            self._next += self._step
            return _r
        
def main():
    for n in inclusive_range(25):
        print(n, end= ' ')
        print()
