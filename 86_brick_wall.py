'''
A simple programme to print THE BRICK WALL on terminal screen.
Tip: I have used `raw` strings.
Author: Sunil Dhaka
'''

GRID_WIDTH=15
GRID_HEIGHT=8

def main():
    for _ in range(GRID_HEIGHT):
        print(r'__|' * GRID_WIDTH)
        print(r'_|_' * GRID_WIDTH)
        
if __name__=='__main__':
    main()