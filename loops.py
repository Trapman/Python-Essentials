# WHILE LOOP
# uses conditional expression to control the loop

secret ='bulldog'
pw = ''

while pw != secret:
    pw = input("What's the secret word?")
    
# FOR LOOP
# uses a sequence to control the loop
animals = ('bulldogs', 'penguins', 'big cats')

for pet in animals:
    print(pet)
    
for pet in range(3):
    print(pet)

# ADDITIONAL LOOP CONTROLS
# continue: shortcuts a loop, and starts it again as if it had reached the end
# break: breaks out of a loop prematurely, code continues after the entire loop structure
# else: executes ONLY if the loop ends normally (e.g. won't execute if it hits a break)

secret ='bulldog'
pw = ''
auth = False
count = 0
max_attempt = 5

while pw != secret:
    count += 1 
    if count > max_attempt:
        break
    pw = input(f"{count}: What's the secret word?")
else:
    auth = True
    
print("Authorized" if auth else "You are not authorized for access")

# same applies to for loop
animals = ('bulldogs', 'penguins', 'big cats')

for pet in animals:
    if pet == 'big cats':
         break
    print(pet)
else:
    print("that's all of the animals that aren't cats")
