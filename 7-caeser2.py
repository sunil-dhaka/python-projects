# add symbols that you want to encrypt or decrypt
SYMBOLES='ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*~1234567890'

def main():
    # try:
    print('Enter the encrypted Caesar cipher message to hack.')
    message=input('> ')

    for i in range(len(SYMBOLES)):
        print(f'Key #{i}({SYMBOLES[i]}):',end=' ')
        print(caeser_hack(message,-i)) # all decryption 
        
    '''except Exception as e:
        print(f'Error: {e}')
        exit()'''

def caeser_hack(message,key):
    symbol_list=[c for c in SYMBOLES]
    encrpted_text=[]
    for c in message:
        if c in symbol_list and c.isupper():
            pos=symbol_list.index(c)
            pos=pos+key
            if pos>=len(symbol_list): # might happen in encryption
                pos=pos-len(symbol_list)
            if pos<0:# might happen in decryption
                pos=pos+len(symbol_list)
            encrpted_text.append(symbol_list[pos])
        else:
            encrpted_text.append(c)
    return ''.join(encrpted_text)

if __name__=='__main__':
    main()