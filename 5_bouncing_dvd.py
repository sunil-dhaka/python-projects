import sys, time, random

try:
    import bext
except ImportError:
    print('get bext module first')
    exit()

WIDTH,HEIGHT=bext.size()

##
WIDTH-=1 #??
##
NO_OF_DVDS=10
PAUSE_TIME=0.1

COLORS = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

UP_RIGHT='ur'
UP_LEFT='ul'
DOWN_RIGHT='dr'
DOWN_LEFT='dl'

DIRECTIONS=(UP_RIGHT,UP_LEFT,DOWN_RIGHT,DOWN_LEFT)

COLOR='color'
X='x'
Y='y'
DIR='direction'

def main():

    # clear screen before starting bounce
    bext.clear()
    # create dvd logos
    dvd_logos=[]
    for i in range(NO_OF_DVDS):
        dvd_item={
            COLOR:random.choice(COLORS),
            X:random.randint(1,WIDTH-4), # why -4??
            Y:random.randint(1,HEIGHT-4),
            DIR:random.choice(DIRECTIONS)
        }
        # Make sure X is even so it can hit the corner.
        if dvd_item[X]%2==1:
            dvd_item[X]-=1
            dvd_logos.append(dvd_item)
        else:
            dvd_logos.append(dvd_item)

    # create bounce
    corner_bounce_count=0
    while True:
        '''
        WIDTH - 3 because 'DVD' has 3 letters
        '''
        for logo in dvd_logos:
            # go to logos current location
            bext.goto(logo[X],logo[Y])
            print('    ',end='')#??

            original_dir=logo[DIR]

            # corner cases
            if logo[X]==0 and logo[Y]==0:
                logo[DIR]=DOWN_RIGHT
                corner_bounce_count+=1
            elif logo[X]==0 and logo[Y]==HEIGHT-1:
                logo[DIR]=UP_RIGHT
                corner_bounce_count+=1
            elif logo[X]==WIDTH-3 and logo[Y]==0:
                logo[DIR]=DOWN_LEFT
                corner_bounce_count+=1
            elif logo[X]==WIDTH-3 and logo[Y]==HEIGHT-1:
                logo[DIR]=UP_LEFT
                corner_bounce_count+=1
            
            # right edge
            elif logo[X]==WIDTH-3 and logo[DIR]==DOWN_RIGHT:
                logo[DIR]=DOWN_LEFT
            elif logo[X]==WIDTH-3 and logo[DIR]==UP_RIGHT:
                logo[DIR]=UP_LEFT
            
            # left edge
            elif logo[X]==0 and logo[DIR]==DOWN_LEFT:
                logo[DIR]=DOWN_RIGHT
            elif logo[X]==0 and logo[DIR]==UP_LEFT:
                logo[DIR]=UP_RIGHT

            # upper edge
            elif logo[Y]==0 and logo[DIR]==UP_RIGHT:
                logo[DIR]=DOWN_RIGHT
            elif logo[Y]==0 and logo[DIR]==UP_LEFT:
                logo[DIR]=DOWN_LEFT
            
            # bottom edge
            elif logo[Y]==HEIGHT-1 and logo[DIR]==DOWN_RIGHT:
                logo[DIR]=UP_RIGHT
            elif logo[Y]==HEIGHT-1 and logo[DIR]==DOWN_LEFT:
                logo[DIR]=UP_LEFT

            # Change color when the logo bounces:
            if logo[DIR]!=original_dir:
                logo[COLOR]=random.choice(COLORS)
            
            # move logos
            if logo[DIR]==UP_RIGHT:
                logo[X]+=2
                logo[Y]-=1
            elif logo[DIR]==UP_LEFT:
                logo[X]-=2
                logo[Y]-=1
            elif logo[DIR]==DOWN_LEFT:
                logo[X]-=2
                logo[Y]+=1
            elif logo[DIR]==DOWN_RIGHT:
                logo[X]+=2
                logo[Y]+=1
    
        # show how many times corner bounces
        bext.goto(5,0)
        bext.fg('blue')
        print('Corner Bounces:',corner_bounce_count,end='')

        # draw logo at new location
        for logo in dvd_logos:
            bext.goto(logo[X],logo[Y])
            bext.fg(logo[COLOR])
            print('DVD',end='')
        bext.goto(0,0)
        # (Required for bext-using programs.)
        sys.stdout.flush()
        time.sleep(PAUSE_TIME)
if __name__=='__main__':
    try:
        main()
    except:
        # when pressed Ctrl-C exit
        print('Stopped DVD bouncing.')
        exit()