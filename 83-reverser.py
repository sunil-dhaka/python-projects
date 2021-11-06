print('Quit to quit the programme.')

while True:
    
    user_input=input('> ')
    if user_input.lower()=='quit':
        exit()
    if user_input=='':
        print('please give a non-empty string to reverse')
    else:
        rev_str=[c for c in user_input]
        rev_str.reverse()
        print(''.join(rev_str))