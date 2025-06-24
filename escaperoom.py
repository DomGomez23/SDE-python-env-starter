import random        #Let's us access python's libary named "random"

name = input('What is your name, Soldier? ')
print(f'Welcome to our "Terminator" escape room, {name} Connor! ')

door_choice = input('Which door shall you choose? Door 1, Door 2 or Door 3? ')
doors = ['Door 1','Door 2', 'Door 3']
random_door_choice = random.choice(doors) 

while door_choice != random_door_choice:
    door_choice = input('Incorrect door, try again: ')    
""" 
if door_choice == 'Door 1':
    print('You are halfway there!')
    print()                     #Skip line
else:
    print('You have picked the wrong door, try again.')
"""

def puzzle():
    print('Now you have entered a dark room and you see a computer glowing in the dark, asking for a correct password with the words:')
    
    password_to_escape = ['T800', 'Sarah Connor', 'John Connor', 'T-1000','Rev-9']
    correct_password = random.choice(password_to_escape)
    
    for password in password_to_escape: 
        print(password)
        
    user_choice = input('You have to pick one password to escape, What password shall you choose? ')
    while user_choice != correct_password:
        user_choice = input('Incorrect password, Try again: ')
    

"""
if user_choice == 'Rev-9':
    print('You have choosen correctly, Goodbye') 
else:
    print('You shall not pass, Try again')
"""    
"""
room = [
  'xxxxx',
  'x..ex',
  'x...x',
  'x...x',
  'xxxxx',
]
"""
"""
room = [
  'xxxxxxxxxxxxxx',
  'x..........pex',
  'xxxxxxxxxxxxxx',
] 
"""

room = [
  'xxxxxxxxxxxxxxxxx',
  'x...p...........x',
  'x...x.x.x.x.xxexx',
  'xxx.x.x.......x.x',
  'x.....xx.x..x...x',
  'xxxxxxxxxxxxxxxxx',
  ]

def move(current_row, current_col, direction):
    new_row = current_row
    new_col = current_col          
    if direction == 'Up':
            new_row = new_row - 1
    elif direction == 'Down':
            new_row = new_row + 1
    elif direction == 'Left':
            new_col = new_col - 1
    elif direction == 'Right':
            new_col = new_col + 1
        
    if room[new_row][new_col] == 'x':
        print('You can not walk there!')
        return current_row, current_col
    if room[new_row][new_col] == 'p':
        puzzle()
    
    return new_row, new_col

def announce_walls(current_row, current_col):
    #Checking direction up
    if room[current_row - 1][current_col] == 'x':
        print('There is a wall up there') 
    #checking direction down
    if room[current_row + 1][current_col] == 'x':
        print('There is a wall down there')
     #checking direction right
    if room[current_row][current_col + 1] == 'x':
         print('There is a wall right there')
     #checking direction left
    if room[current_row][current_col - 1] == 'x':
         print('There is a wall to the left')


player_row = 1
player_col = 1

print('Now you are in a maze, you have to find a way out')
print(f'Your row is {player_row}')
print(f'Your col is {player_col}')
while room[player_row][player_col] != 'e':
    direction_choice = input('In what direction shall you move? Up? Down? Left? or Right? ')
    player_row, player_col = move(player_row, player_col, direction_choice)
    print(f'Your row is {player_row}')
    print(f'Your new col is {player_col}')
    
    
print ('Correct! You have succsesfully got out of the Escape room, Goodbye!')