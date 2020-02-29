# CLASSES ####################

class Bulldog:
    sound = "woof! I'm hungry!!"
    movement = 'walks like a bully.'
    
    def woof(self):        # first parameter is always self, but you can name it whatever you want
        print(self.sound)  # self is a reference to the object
        
    def move(self):
        print(self.movement)
        
def main():
    buford = Bulldog()
    buford.woof
    buford.move
    
if __name__ == '__main__': main()

# CONSTRUCTING AN OBJECT ###################
class Animal:
    def __init__(self, type, name, sound):  # 'initializer' or constructor. always self, followed by whatever object variables you want to include
        self._type = type
        self.name = name
        self.sound = sound
        
    def type(self):
        return self._type
    
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
    
if __name__ = '__main__': main()

##
