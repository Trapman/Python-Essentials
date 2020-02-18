# SHEBANG LINE ###########################
# basically a unix based system that allows the script to be invoked from the command line

#!/usr/bin/env python3   #  #! is the shebang, then the rest is the pathway
# I think this won't work on PC; Mac only

# CONDITIONAL STATEMENTS #################################
x = 100
y = 50
if x > y:
  print("X is greater than Y, tbh")
elif x < y:
  print("Naw, X is less than Y, tbqh")
else:
  print("Cool out YB, they're equal or something else is going on.")
  
#WHILE LOOPS ############################################
# tests a conditional expression in the body of the loop is executed while the condition remains True
# basic example [1]
words = ["mega", "trap", "hoang", "brad", "dan"]

n = 0
while (n<5):
  print(words[n])
  n += 1
  
# simple fibonnaci series example [2]
# the sum of two elements defines the next set

a, b = 0, 1
while b < 1000:
  print(b, end = ' ', flush = True)
  a, b = b, a + b
  
print() # line ending


#FOR LOOPS #########################################
# iterates over a sequence, and the body of the loop is executed for each element of the sequence and until the sequence is exhausted
# basic example[1]
words = ["mega", "trap", "hoang", "brad", "dan"]

for i in words:
  print(i)
  
# FUNCTIONS #################################################
# basic bare bones function [1]   # function(99) will print 99, and so forth
def function(n):
  print(n)   

# using a default value
def function(n = 1):
  print(n)
 
# so now the program will default to printing 1 unless you pass in a value for n
    
# working example of checking for a prime number [2]
def isprime(n):
  if n<=1:
    return False
  for x in range(2, n):
    if n % x == 0:
      return False
  else:
    return True
    
n = 5
if isprime(n):
  print("this is a prime number")
else:
  print("this is not a prime number")

# creating a function that lists out prime number [3]
def list_primes():
  for n in range(100):
    if  isprime(n):
      print(n, end =' ', flush = 'True')

# CLASSES ##########################################
class Duck:
  def quack(self):         # function 1 inside class (i.e. class variable 1)
    print("QUACK!!!")
    
  def walk(self):          #function 2 inside class (i.e. class variable 2)
     print("It walks like a duck.")
      
  def main():
    donald = Duck()
    donald.quack()
    donald.walk()
    
  if __name__ == '__main__': main()

# or you can do it like this
class Duck:
  sound = "QUACK!!!"
  walking = "Walks like a duck.)
  
  def quack(self):         # function 1 inside class (i.e. class variable 1)
    print(self.sound)
    
  def walk(self):          #function 2 inside class (i.e. class variable 2)
     print(self.walking)
      
  def main():
    donald = Duck()
    donald.quack()
    donald.walk()    






