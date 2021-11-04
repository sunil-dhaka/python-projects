import random

HOUSE_FEE_PERCENT=0.10
START_MONEY=5000
ODD=1

LOST='\033[1;31mLOST\033[m'
WON='\033[1;32mWON\033[m'

# have to edit appropriately
# useful link: https://blog.busuu.com/japanese-numbers/
NO_OF_DICE_FACES=6
JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN', 4:'SHI', 5: 'GO', 6: 'ROKU'}

def main():
    print('''
In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.
    ''')
    curr_money=START_MONEY
    
    while True:
        print(f'You have {curr_money} money. How much do you bet? (or QUIT)')
        
        while True:
            bet=input('> ')
            if bet.lower()=='quit':
                exit()
            if bet.isnumeric():
                if int(bet)>curr_money:
                    print('You do not have enough to make that bet.')
                elif int(bet)==0:
                    print('Dude! W*F, no money is not allowed in this casino.')
                else:
                    bet_amount=int(bet)
                    break
                
            else:
                print('Please enter a number.')

        print('''
The dealer swirls the cup and you hear the rattle of dice.
The dealer slams the cup on the floor, still covering the
dice and asks for your bet.

    CHO (even) or HAN (odd)?
        ''')
        while True:
            choice=input('> ').lower()
            if choice=='han' or choice=='cho':
                break
            print('Please enter either "CHO" or "HAN".')
        
        first_dice=random.randint(1,NO_OF_DICE_FACES)
        second_dice=random.randint(1,NO_OF_DICE_FACES)
        total=first_dice+second_dice
        

        # result #

        print('The dealer lifts the cup to reveal:')

        print(f'''
        {JAPANESE_NUMBERS[first_dice]} - {JAPANESE_NUMBERS[second_dice]}
        {first_dice} - {second_dice}
        ''')

        if (total%2==0 and choice=='cho') or (total%2!=0 and choice=='han'):
            print(f'''
You {WON}! You take {round(bet_amount*ODD)} mon.
The house collects a {HOUSE_FEE_PERCENT*bet_amount} mon fee.
        ''')    
            curr_money+=round(bet_amount*(ODD-HOUSE_FEE_PERCENT))
        else:
            print(f'You {LOST}!')
            curr_money-=round(bet_amount*ODD)

        if curr_money==0:
            print(f'You {LOST} all youe money. Too bad.')
            exit()

if __name__=='__main__':
    main()