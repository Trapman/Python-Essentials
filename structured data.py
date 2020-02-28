# DATA STRUCTURES

# LIST #############################
# mutable
# list = []

#ex iterate through a list and print elements in order
def main():
    game = ['sixers', 'mavs', 'lakers', 'bucks', 'clippers']
    #print(game[1:3]) # use this to index a specific game(s) in the list
    # i = game.index('bucks') # use this to search a list using indexing method
    # print(game[i]) # use this to print above
    # game.append('raptors') # use this to add a game to the list
    # game.insert(0, 'raptors') # use this to add a game to a specific index of list
    # game.remove('sixers") # use this to remove a specific item
    # game.pop() # use to remove a game from end of list
    # game.pop(3) # remove game at particular index
    # del game [3] # can also use delete to remove game at particualr index 
    # print(', '.join(game)) # use to join commas between games
    print_list(game)
    
def print_list(o):
    for i in o: 
        print(i, end=' ', flush = True)
    print()
    
if __name__ == '__main__': main()

# TUPLE #############
# immutable
# otherwise works exactly like a list
# tuple = ()

def main():
    game = ('sixers', 'mavs', 'lakers', 'bucks', 'clippers')
    print_list(game)
    
def print_list(o):
    for i in o: 
        print(i, end=' ', flush = True)
    print()
    
if __name__ == '__main__': main()

# DICT ##########################
# dict = {k : v}

def main():
    teams = { 'sixers' : 'average', 'bucks' : 'elite', 'clippers' : 'elite', 
             'mavs':'above average', 'pistons':'brutal'}
    #for k, v in teams.items(): # use items() method to print out the keys, values
        #print(f'{k}: {v}')
    print_dict(teams)

    
def print_dict(o):
    for x in o: print(f'{x}: {o[x]}')
    
if __name__ == '__main__' : main()

# creating a dict using dict constructor and key-word arguments
teams = dict(sixers = 'average', bucks = 'elite', clippers = 'elite', 
             mavs = 'above average', pistons = 'brutal')

# items() method
def main():
    teams = { 'sixers' : 'average', 'bucks' : 'elite', 'clippers' : 'elite', 
             'mavs':'above average', 'pistons':'brutal'}
    for k, v in teams.items():  
        print(f'{k}: {v}')
    
def print_dict(o):
    for k, v in o.items(): print(f'{k}: {v}')
    
if __name__ == '__main__' : main()

# keys() and values() methods ############
def main():
    teams = { 'sixers' : 'average', 'bucks' : 'elite', 'clippers' : 'elite', 
             'mavs':'above average', 'pistons':'brutal'}
    for k in teams.keys():  # or for v in teams.values()
        print(k)
    
def print_dict(o):
    for k, v in o.items(): print(f'{k}: {v}')
    
if __name__ == '__main__' : main()

# use indexing to select specific keys
def main():
    teams = { 'sixers' : 'average', 'bucks' : 'elite', 'clippers' : 'elite', 
             'mavs':'above average', 'pistons':'brutal'}
    for v in teams.values():
        print(teams['sixers']
    
def print_dict(o):
    for k, v in o.items(): print(f'{k}: {v}')
    
if __name__ == '__main__' : main()

# assign different values:
def main():
    teams = { 'sixers' : 'average', 'bucks' : 'elite', 'clippers' : 'elite', 
             'mavs':'above average', 'pistons':'brutal'}
    teams['sixers'] = 'elite  
    teams['spurs'] = 'average' #add in an entirely new key/value pair
    
def print_dict(o):
    for k, v in o.items(): print(f'{k}: {v}')
    
if __name__ == '__main__' : main()

# use conditionals to check if something is there
def main():
    teams = { 'sixers' : 'average', 'bucks' : 'elite', 'clippers' : 'elite', 
             'mavs':'above average', 'pistons':'brutal'}
    print('found!' if 'lakers' in teams else 'nope!')
    
def print_dict(o):
    for k, v in o.items(): print(f'{k}: {v}')
    
if __name__ == '__main__' : main()

# use get() method if you want to search for something and return None instead of an error if it doesn't exist
def main():
    teams = { 'sixers' : 'average', 'bucks' : 'elite', 'clippers' : 'elite', 
             'mavs':'above average', 'pistons':'brutal'}
    print(team.get('lakers'))  
    
def print_dict(o):
    for k, v in o.items(): print(f'{k}: {v}')
    
if __name__ == '__main__' : main()

# SETS #####################
# like a list, but doesn't allow duplicate elements
 def main():
     a = set('We are checking for duplicate letters.')
     b = set('We might have some extra letters here.')
     print_set(a)         # default, not sorted
     print_set(sorted(b)) # sorted() option
    
def print_set(o):
    print('{', end = '')
    for x in o: print(x, end = '')
    print('}')
    
if __name__ == '__main__' : main()

# checking membership: 
def main():
     a = set('We are checking for duplicate letters.')
     b = set('We might have some extra letters here.')
     print_set(a - b) # finds members that are in set a that are NOT in b
     # print_set(a | b) in set a or b or both
     # print_set(a ^ b) # in a or b but not both
     # print_set(a & b) # in both a and b 
def print_set(o):
    print('{', end = '')
    for x in o: print(x, end = '')
    print('}')
    
if __name__ == '__main__' : main()

# LIST COMPREHENSION #############
def main():
    seq = range(11)
    seq2 = [x * 2 for x in seq] # list comp of the numbers in seq multiplied by 2
    #seq3 = [x for x in seq if x % 3 !=0] # prints numbers in seq that aren't divisible by 3
    #seq4 = [(x, x**2) for x in seq] # create a tuple of each element and its square
    #seq5 = {x: x**2 for x in seq} # same as above but create dict
    print_list(seq)
    print_list(seq2)
    
def print_list(o):
    for x in o: print(x, end = ' ')
    print()
    
if __name__ == '__main__' : main()
