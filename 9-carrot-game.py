# no need to check import as it is comes with python
import sys,random

SMILE=chr(9786)
RED_BOX = [
    '  __________',
    ' /         /|',
    '+---------+ |',
    '|   RED   | |',
    '|   BOX   | /',
    '+---------+/'
]

GOLD_BOX = [
    '  __________',
    ' /         /|',
    '+---------+ |',
    '|   GOLD  | |',
    '|   BOX   | /',
    '+---------+/'
]

OPEN_EMPTY_RED=[
    '   _________ ',
    '  |         |',
    '  |         |',
    '  |         |'
]

OPEN_EMPTY_RED.extend(RED_BOX)

OPEN_EMPTY_GOLD=[
    '   _________ ',
    '  |         |',
    '  |         |',
    '  |         |'
]

OPEN_EMPTY_GOLD.extend(GOLD_BOX)

OPEN_CARROT_RED=[
    '   ___VV____ ',
    '  |   VV    |',
    '  |   ||    |',
    '  |   ||    |'
]

OPEN_CARROT_RED.extend(RED_BOX)

OPEN_CARROT_GOLD=[
    '   ___VV____ ',
    '  |   VV    |',
    '  |   ||    |',
    '  |   ||    |'
]

OPEN_CARROT_GOLD.extend(GOLD_BOX)

def main():
    print('''
This is a bluffing game for two human players. Each player has a box.
One box has a carrot in it. To win, you must have the box with the
carrot in it.

This is a very simple and silly game.

The first player looks into their box (the second player must close
their eyes during this.) The first player then says "There is a carrot
in my box" or "There is not a carrot in my box". The second player then
gets to decide if they want to swap boxes or not.
    ''')

    input('Press Enter to begin...')
    while True:

        player_1=input('Human player 1, enter your name: ')
        if player_1!='':
            break
        print('Give a Valid Name Mr. Empty')
    while True:

        player_2=input('Human player 2, enter your name: ')
        if player_2!='':
            break
        
        print('Give a Valid Name Mr. Empty')

    box_type=random.randint(1,2)

    print('HERE ARE TWO BOXES:')
    print('\n'.join(RED_BOX))
    print(player_1.split(' ')[0].center(len(RED_BOX[0]),' '))
    
    print('\n'.join(GOLD_BOX))
    print(player_2.split(' ')[0].center(len(GOLD_BOX[0]),' '))

    print('''
{p1}, you have a RED box in front of you.
{p2}, you have a GOLD box in front of you.
    '''.format(p1=player_1,p2=player_2))

    print('''
{p1}, you will get to look into your box.
{p2}, close your eyes and don't look!!!
    '''.format(p1=player_1,p2=player_2))

    input(f'When {player_2} has closed their eyes, press Enter...')

    print(f'{player_1} here is the inside of your box:')

    if box_type==1:
        print('\n'.join(OPEN_CARROT_RED))
        print(('(carrot)'+SMILE).center(len(OPEN_CARROT_RED[0]),' '))
        print(player_1.split(' ')[0].center(len(OPEN_CARROT_RED[0]),' '))
        
        print('\n'.join(GOLD_BOX))
        print(player_2.split(' ')[0].center(len(GOLD_BOX[0]),' '))
    else:
        print('\n'.join(OPEN_EMPTY_RED))
        print('(no carrot)'.center(len(OPEN_CARROT_RED[0]),' '))
        print(player_1.split(' ')[0].center(len(OPEN_EMPTY_RED[0]),' '))
        
        print('\n'.join(GOLD_BOX))
        print(player_2.split(' ')[0].center(len(GOLD_BOX[0]),' '))
    
    input('Press Enter to begin...')
    print('\n'*60)

    print(f'{player_1}, tell {player_2} to open their eyes.')
    input('Press Enter to begin...')
    print('''
{p1}, say one of the following sentences to {p2}.
  1) There is a carrot in my box.
  2) There is not a carrot in my box.
        '''.format(p1=player_1,p2=player_2))

    input('Then press Enter to continue...')

    
    while True:
        print(f'{player_2}, do you want to swap boxes with {player_1}? YES/NO')
        swap_input=input('> ').lower()
        if swap_input.startswith('y') or swap_input.startswith('n'):
            break

    if swap_input.startswith('y'):
        print('HERE ARE TWO BOXES:')

        print('\n'.join(GOLD_BOX))
        print(player_1.split(' ')[0].center(len(GOLD_BOX[0]),' '))

        print('\n'.join(RED_BOX))
        print(player_2.split(' ')[0].center(len(RED_BOX[0]),' '))
        input('Press Enter to reveal the winner...')
        if box_type==1:
            print('\n'.join(OPEN_EMPTY_GOLD))
            print(player_1.split(' ')[0].center(len(OPEN_EMPTY_GOLD[0]),' '))
            
            print('\n'.join(OPEN_CARROT_RED))
            print(player_2.split(' ')[0].center(len(OPEN_CARROT_RED[0]),' '))
            print('''
{p} is the winner!
Thanks for playing!
            '''.format(p=player_2))
        else:
            print('\n'.join(OPEN_EMPTY_GOLD))
            print(player_1.split(' ')[0].center(len(OPEN_EMPTY_GOLD[0]),' '))
            
            print('\n'.join(OPEN_EMPTY_RED))
            print(player_2.split(' ')[0].center(len(OPEN_EMPTY_RED[0]),' '))
            print('''
{p} is the winner!
Thanks for playing!
            '''.format(p=player_1))
    else:
        print('HERE ARE TWO BOXES:')
        print('\n'.join(RED_BOX))
        print(player_1.split(' ')[0].center(len(RED_BOX[0]),' '))
        
        print('\n'.join(GOLD_BOX))
        print(player_2.split(' ')[0].center(len(GOLD_BOX[0]),' '))
        input('Press Enter to reveal the winner...')

        if box_type==1:
            print('\n'.join(OPEN_CARROT_RED))
            print(player_1.split(' ')[0].center(len(OPEN_CARROT_RED[0]),' '))
            
            print('\n'.join(OPEN_EMPTY_GOLD))
            print(player_2.split(' ')[0].center(len(OPEN_EMPTY_GOLD[0]),' '))
            print('''
{p} is the winner!
Thanks for playing!
            '''.format(p=player_1))
        else:
            print('\n'.join(OPEN_EMPTY_RED))
            print(player_1.split(' ')[0].center(len(OPEN_EMPTY_RED[0]),' '))
            
            print('\n'.join(OPEN_EMPTY_GOLD))
            print(player_2.split(' ')[0].center(len(OPEN_EMPTY_GOLD[0]),' '))
            print('''
{p} is the winner!
Thanks for playing!
            '''.format(p=player_2))

if __name__=='__main__':
    main()