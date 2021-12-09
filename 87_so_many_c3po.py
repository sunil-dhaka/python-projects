'''
A simple programme to print THE C3PO WALL on terminal screen.
Tip: I have used `raw` strings.
Author: Sunil Dhaka
'''

GRID_WIDTH=5
GRID_HEIGHT=3

def main():
    for _ in range(GRID_HEIGHT):
        print(r'/ ___ \ ^ ' * GRID_WIDTH)
        print(r' /   \ VVV' * GRID_WIDTH)
        print(r'|() ()|   ' * GRID_WIDTH)
        print(r' \ ^ / ___' * GRID_WIDTH)
        print(r'\ VVV /   ' * GRID_WIDTH)
        print(r')|   |() (' * GRID_WIDTH)
        
if __name__=='__main__':
    main()