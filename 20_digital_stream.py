import random, sys, time, shutil

WIDTH,_=shutil.get_terminal_size((20,80)) # (20,80) are fallback values
# We can't print to the last column on Windows without it adding a
# newline automatically, so reduce the width by one:
WIDTH-=1

MATRIX_STR=('0','1','#','@','!','$',chr(1000))
COL_DENSITY=0.03
MIN_LEN=7
MAX_LEN=14
PAUSE=0.1

def main():
    print('press ctrl-c to stop\n\n')
    time.sleep(2)

    columns=[0]*WIDTH

    while True:
        # set counter for each col
        # this basically checks wether to start string 
        # or not on a particular col in each run
        for i in range(WIDTH):
            if columns[i] == 0:
                if random.random() < COL_DENSITY:
                    columns[i]=random.randint(MIN_LEN,MAX_LEN)
            # Display an empty space or a 1/0 character.
            if columns[i] > 0:
                print(random.choice(MATRIX_STR),end='',flush=True)
                # imp step
                columns[i]-=1
            else:
                print(' ',end='',flush=True)
        print()
        # sys.stdout.flush()
        time.sleep(PAUSE)

if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()