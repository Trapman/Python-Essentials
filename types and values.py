# STRING TYPES ############################
# use quote marks ' ' OR " "
x = 'seven'
print(type(x))  # returns string 

# you can run methods on strings since they're object. Here are some common ones:
.capitalize()
.upper()
.lower()

# f string
a = 8
b = 9
x = f'seven {a} {b}'
print(x)                   # returns x is seven 8 9


# NUMERIC TYPES ############################
# INTEGERS ################################################
int()
x = 7


# FLOATING #################################################
  
# when dealing with money, use this:
  from decimal import *
  
#BOOLEAN TYPE ########################################
#True/Falso

# SEQUENCE TYPES ###########################################################
# list = [] #############################################################
x = [1,2,3,4,5]
for i in x:
    print(i)
# reassigning and indexing: use []
x[3] = 99  # reassigns item[3] to 99

# tuple = () ###############################################################
# you can't reassign a tuple, they're immutable
x = (1,2,3,4,5)
for i in x:
    print(x)

# also, you can create a sequence using range()
# syntax: range(start, stop, step)
# also immutable
x = range(5)
for i in x:
    print(x)
    
x = range(5, 50, 5) 
for i in x:
    print(i)
    
#to make it mutable, add in list()
x = list(range(5))
x[2] = 42
for i in x:
    print(i)
    
# dictionary x = {key : value} ####################################################################
x = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five' :5}
for k, v in x.items():
    print('k: {}, v: {}'.format(k, v)) #he uses this .format() method a lot
  
# dicts are mutable
x = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five' :5}
x['three'] = 42   # you can change value like this
for k, v in x.items():
    print('k: {}, v: {}'.format(k, v))
    
# TYPE() and ID() ###################################################################################
x = (1,'two',3.0,[4, 'four'],5) 
print(x)   
print(type(x[2]))
print(id(x[2]))

# how to check if something is a list/tuple/etc.
# use isinstance()
if isinstance(x, tuple):
    print('yes it is a tuple')
elif isinstance(x, list):
    print('wait, actually it is a list')
else:
    print('nope!')
