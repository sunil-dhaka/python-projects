print('What size multiplication table you want?')
DIGIT=int(input())

def main():
    print(f'multiplication table of size {DIGIT}x{DIGIT}')
    print(' '*2+ '|',end='  ')
    for i in range(DIGIT):
        number=str(i+1)
        print(' '*4+'\b'*len(number)+number,end='  ')
    print()
    # here 6 is set to make it look nice
    print('--+'+'-'.rjust(6*DIGIT,'-'))

    for i in range(DIGIT):
        mult_line(i+1)
    
    return None

def mult_line(number):
    print(' '*2+'\b'*len(str(number))+str(number)+ '|',end='  ')
    for i in range(DIGIT):
        mult_number=str((i+1)*number)
        print(' '*4+'\b'*len(mult_number)+mult_number,end='  ')
    print()

    return None

if __name__=='__main__':
    main()