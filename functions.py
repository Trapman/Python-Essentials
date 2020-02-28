def main():
    bulldog()
    
def bulldog():
    print('feed me!')

if __name__ == '__main__': main() # __name__ is a special variable that returns the name of the current module
#####
def main():
    bulldog(3)
    
def bulldog(n):
    print(f'{n}feed me!')

if __name__ == '__main__': main()

# FUNCTION ARGUMENTS
def main():
    bulldog(5, 6)
    
def bulldog(a, b, c = 0):    # c represents a default argument
    print('feed me!')
    print(a, b, c)

if __name__ == '__main__': main()

# ARGUMENT LISTS

def main():
    kitten('meow', 'grrr', 'purr')
    
def kitten(*args):     # variable length argument list. It's a tuple
    if len(args):
        for s in args:
            print(s)
        else:
            print('meow')
            
if __name__ == '__main__': main()

# another example to get the same result:
def main():
    x = ('meow', 'grrr', 'purr')
    kitten(*x)
    
def kitten(*args):     # variable length argument list. It's a tuple
    if len(args):
        for s in args:
            print(s)
        else:
            print('meow')
            
if __name__ == '__main__': main()

# KEY WORD ARGUMENTS #############
# like list arguments, but are dicts rather than tuples
# allows function to have a variable number of named arguments

def main():
    kitten(Buffy = 'meow', Zilla = 'grr', Angel = 'rawr')
    
def kitten(**kwargs):
    if len(kwargs):
        for k in kwargs:
            print('Kitten {} says {}.format(k, kwargs[k]))
        else:
            print('meow')
            
if __name__ == '__main__': main()

# another example to get the same result:
def main():
    x = dict(Buffy = 'meow', Zilla = 'grr', Angel = 'rawr')
    kitten(**x)
    
def kitten(**kwargs):
    if len(kwargs):
        for k in kwargs:
            print('Kitten {} says {}.format(k, kwargs[k]))
        else:
            print('meow')
            
if __name__ == '__main__': main()

# RETURN VALUES #################
def main():
    x = bulldog()
    print(type(x), x)
    
def bulldog():
    print("I'm hungry!")
    return dict(buford = 5, henley = 4, emi = 4)

if __name__ == '__name__': main()

# GENERATORS ###################
# instead of returning a single value, it returns a stream of values
# example: build our own version of range() that includes all numbers inclusive
def main():
    for i in inclusive_range():
        print(i, end = ' ')
    print()
    
def inclusive_range(*args):
    numargs = len(args)
    start = 0
    stop = 1
    
    #initiate parameters
    if numargs < 1:
        raise TypeError(f'expected at least 1 argument, got {numargs}')
    elif numargs == 1:
        stop == args[0]
    elif numargs == 2:
        (start, stop) = args
    elif numargs == 3:
        (start, stop, step) = args
    else:
        raise TypeError(f'expected at most 3 arguments, got {numargs}')
        
# DECORATORS #################
# specical type of function that returns a wrapper function
def f1(f):
    def f2():
        print('this is before the function call')
        f()
        print('this is after the function call')
    return f2

@f1
def f3():
    print('this is f3)
    
f3()

# Example
import time

def elapsed_time(f):
    def wrapper():
        t1 = time.time()
        f()
        t2 = time.time()
        print(f'Elapsed time: {(t2 - t1) * 1000} ms')
        
@elapsed_time
def big_sum():
    num_list = []
    for num in range(0, 10000)):
        num_list.append(num)
    print(f'Big sum: {sum(num_list)}')
    
def main():
    big_sum()
    
if __name__ == '__main__': main()
