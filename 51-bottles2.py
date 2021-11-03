print('From where to start count?')
try:
    DIGIT=int(input())
except Exception as e:
    print(f'Error >> {e}')
    exit()
try:
    import sys,time,random
except Exception as e:
    print(f'error message >> {e}')
    exit()

def main():
    try:
        bottles_count=DIGIT
        while True:
            print(str(bottles_count),end=' ')
            slow_print('bottles of milk on the wall')
            print(',')

            print(str(bottles_count),end=' ')
            slow_print('bottles of milk')
            print(',')

            slow_print('Take one down, pass it around')
            print(',')

            print(str(bottles_count-1),end=' ')
            slow_print('bottles of milk on the wall')
            print('!,')

            print()
            if bottles_count==1:
                break
            bottles_count-=1
    except:
        sys.exit()

def slow_print(text,print_speed=0.1):
    text=[t for t in text]

    # modify text randomly
    edit_counts=random.randint(0,3)
    if edit_counts!=0:
        edit_place=[]
        for i in range(edit_counts):
            edit_type=(random.randint(1,3))
            edit_place=random.randint(0,len(text)-1)
            if text[edit_place]!=' ':
                if edit_type==1:
                    text[edit_place]=' '
                elif edit_type==2:
                    text[edit_place]=text[edit_place].upper()
                elif edit_type==3:
                    text.insert(edit_place,text[edit_place])
                    
    # slow print to the screen using flush                    
    for c in text:
        print(c,end='',flush=True) 
        time.sleep(print_speed)

if __name__=='__main__':
    main()