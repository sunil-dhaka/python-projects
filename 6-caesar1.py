try:
    import sys
except Exception as error:
    print(f'Error >> {error}')

# add symbols that you want to encrypt or decrypt
SYMBOLES='ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*~1234567890'

def main():
    try:
        print('''
The Caesar cipher encrypts letters by shifting them over by a
key number. For example, a key of 2 means the letter A is
encrypted into C, the letter B encrypted into D, and so on.
        ''')
        # take correct inputs
    
        while True:
            print('Do you want to (e)ncrypt or (d)ecrypt?')
            ed_input=input('> ')[0].lower()

            if ed_input=='e' or ed_input=='d':
                break

            print('Please enter the letter e or d.')

        while True:
            print(f'Please enter the key (0 to {len(SYMBOLES)}) to use.')
            key=input('> ')

            if key.isnumeric():
                if int(key)<len(SYMBOLES) and int(key)>-1:
                    break

        if ed_input=='e':
            print('Enter the message to encrypt.')
            message=input('> ').upper()
            print(encrypt_decrypt(message,int(key)))
        else:
            print('Enter the message to decrypt.')
            message=input('> ').upper()
            print(encrypt_decrypt(message,-int(key)))
    except:
        sys.exit()

def encrypt_decrypt(message,key):
    symbol_list=[c for c in SYMBOLES]
    encrpted_text=[]
    for c in message:
        if c in symbol_list:
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

'''
# this func uses ord() and chr() to convert into numeric and char
def encrypt_decrypt(message,key):
    text=[c for c in message]
    encrpted_text=[]
    start_ord=ord('A')
    for i,char in enumerate(text):
        ord_of_char=ord(char)
        if ord_of_char>64 and ord_of_char<91:
            mod_ord=start_ord+((ord_of_char+key-start_ord)%26)
            encrpted_text.append(chr(mod_ord))
        else:
            encrpted_text.append(char)
        
    return ''.join(encrpted_text)
'''

if __name__=='__main__':
    main()