try:
    import sys,random,time
except Exception as error:
    print(f'Error >> {error}')

def main():
    print('Press Ctrl+C to stop.')
    time.sleep(2)
    try:
        diamond_size=1
        while True:
            for i  in range(2):
                diamond_type=random.randint(1,2)
                if diamond_type==1:
                    filled_diamond(diamond_size)
                else:
                    simple_diamond(diamond_size)
                time.sleep(1)
                print()
            diamond_size+=1

    except:
        sys.exit()

def filled_diamond(diamond_size):
    for i in range(diamond_size):
        print(' '.rjust(diamond_size-i),end='')
        print('/'*(i+1),end='')
        print('\\'*(i+1))

    for i in range(diamond_size):
        print(' '.rjust(i+1),end='')
        print('\\'*(diamond_size-i),end='')
        print('/'*(diamond_size-i))

def simple_diamond(diamond_size):
    
    for i in range(diamond_size):
        print('/'.rjust(diamond_size-i),end='')
        print('\\'.rjust(2*i+1))

    for i in range(diamond_size):
        print('\\'.rjust(i+1),end='')
        print('/'.rjust(2*(diamond_size-i-1)+1))


if __name__=='__main__':
    main()