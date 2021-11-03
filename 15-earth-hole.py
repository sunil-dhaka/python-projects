CHAR=chr(8776)

try:
    import sys,random,time
except Exception as error:
    print(f'Error >> {error}')

def main():
    print('Press Ctrl+C to stop.')
    time.sleep(2)
    try:
        left_len=15
        total_len=50
        middle_len=10
        while True:
            print((CHAR*left_len)+(' '*middle_len).ljust(total_len,CHAR))
            change_len=random.randint(-1,1)
            left_len+=change_len
            total_len-=change_len
            time.sleep(1)
    except:
        sys.exit()

if __name__=='__main__':
    main()