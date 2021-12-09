'''
A simple programme to print hex grid on terminal screen.
Tip: I have used `raw` strings.
Author: Sunil Dhaka
'''

GRID_WIDTH=20
GRID_HEIGHT=16

def main():
    for _ in range(GRID_HEIGHT):
        for _ in range(GRID_WIDTH):
            print(r'/ \_',end='')
        print()
        for _ in range(GRID_WIDTH):
            print(r'\_/ ',end='')
        print()
    
if __name__=='__main__':
    main()