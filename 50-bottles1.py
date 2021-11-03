DIGIT=99

try:
    import sys,time
except Exception as e:
    print(f'error message >> {e}')
    exit()

def main():
    try:
        bottles_count=DIGIT
        while True:
            print('''
{first_count} bottles of milk on the wall,
{first_count} bottles of milk,Take one down, 
pass it around,
{second_count} bottles of milk on the wall!
            '''.format(first_count=bottles_count,second_count=bottles_count-1))
            time.sleep(5)
            if bottles_count==1:
                break
            bottles_count-=1
    except:
        sys.exit()


if __name__=='__main__':
    main()