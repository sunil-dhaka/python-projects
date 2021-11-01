import random

# global vars
DIGIT_LEN=3
MAX_CHANCES=10

# main function for the game
def guess():

    print('''
I am thinking of a {}-digit number. Try to guess what it is.
Here are some clues:
When I say:         That means:
Pico                One digit is correct but in the wrong position.
Fermi               One digit is correct and in the right position.
Bagels              No digit is correct.
\n
I have thought up a number.
You have 10 guesses to get it.
    '''.format(DIGIT_LEN))

    while True:
        secret_num=get_secret_num()
        
        i=0
        while (i<MAX_CHANCES):
            print(f'Guess #{str(i+1)}')
            guess_num=input()
            if guess_num.isalnum() and len(guess_num)==DIGIT_LEN:
                if guess_num != '' and int(guess_num)==secret_num:
                    if i>4:
                        print(f'Well! After {str(i+1)} many tries you got it correct.')
                    else:
                        print(f'Wow! You got it in just {str(i+1)} many tries.')
                    break
                else:
                    print(get_clues(secret_num,guess_num))
                i+=1
            else:
                print(f'Nah man! at least give a valid {DIGIT_LEN} digit number.')    

        print(f'Secret number was {str(secret_num)}')
        
        print("Let's see if can do better. (y|N) ?")
        play_game=input()
        if play_game.lower()=='n':
            break
        else:
            pass

def get_clues(secret_num,guess_num):
    s_nums=[c for c in str(secret_num)]
    g_nums=[c for c in guess_num]

    # previous version for clue condition
    '''
    if any(s in guess_num for s in s_nums):
        if any(s==g for s,g in zip(s_nums,g_nums)):
            return 'Fermi'
        else:
            return 'Pico'
    else:
        return 'Bagels'
    '''
    
    clues_list=list()
    for s,g in zip(s_nums,g_nums):
        if g==s:
            clues_list.append('Fermi')
        elif g in s_nums:
            clues_list.append('Pico')

    if len(clues_list)>0:
        return ' '.join(clues_list)
    else:
        return 'Bagels'


def get_secret_num():
    min_digit=int('1' + '0'*(DIGIT_LEN-1))
    max_digit=int('9'*DIGIT_LEN)
    return random.randint(min_digit,max_digit)

if __name__=='__main__':
    guess()