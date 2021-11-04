try:
    import time
except Exception as e:
    print(f'Error: {e}')
    exit()

PAUSE=0.1
def main():
    print('''
The Collatz sequence is a sequence of numbers produced from a starting
number n, following three rules:

1) If n is even, the next number n is n / 2.
2) If n is odd, the next number n is n * 3 + 1.
3) If n is 1, stop. Otherwise, repeat.

It is generally thought, but so far not mathematically proven, that
every starting number eventually terminates at 1.
    ''')

    print('Enter a starting number (greater than 0) or QUIT:')
    user_input=input('> ').lower()
    if user_input=='quit':
        exit()
    if user_input.isnumeric() and int(user_input):
        start_number=int(user_input)
    else:
        print('You must enter an integer greater than 0.')
        exit()
    
    next_number=start_number
    print(next_number,end=', ',flush=True)
    time.sleep(PAUSE)
    while next_number!=1:
        if next_number%2==0:
            next_number=next_number//2
            print(next_number,end=', ',flush=True)
            time.sleep(PAUSE)
        else:
            next_number=3*next_number+1
            print(next_number,end=', ',flush=True)
            time.sleep(PAUSE)
    print()

if __name__=='__main__':
    main()