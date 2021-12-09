'''
A simple programme to print THE SHINING CARPET on terminal screen.
Tip: I have used `raw` strings.
Author: Sunil Dhaka
'''

GRID_WIDTH=5
GRID_HEIGHT=4
'''
Also can use multiple of string rather than a for loop
Like print(r'- \ \ \_/ __'*GRID_WIDTH)
'''
def main():
    for _ in range(GRID_HEIGHT):
        for _ in range(GRID_WIDTH):
            print(r'_ \ \ \_/ __',end='')
        print()
        for _ in range(GRID_WIDTH):
            print(r' \ \ \___/ _',end='')
        print()
        for _ in range(GRID_WIDTH):
            print(r'\ \ \_____/ ',end='')
        print()
        for _ in range(GRID_WIDTH):
            print(r'/ / / ___ \_',end='')
        print()
        for _ in range(GRID_WIDTH):
            print(r'_/ / / _ \__',end='')
        print()
        for _ in range(GRID_WIDTH):
            print(r'__/ / / \___',end='')
        print()
        
if __name__=='__main__':
    main()