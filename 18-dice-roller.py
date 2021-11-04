try:
    import random
except ImportError:
    print(ImportError)
    exit()

INVALID_LINE='Invalid input. Enter something like "3d6" or "1d10+2".'

def main():

    print('''
Enter what kind and how many dice to roll. The format is the number of
dice, followed by "d", followed by the number of sides the dice have.
You can also add a plus or minus adjustment.

Examples:
  3d6 rolls three 6-sided dice
  1d10+2 rolls one 10-sided die, and adds 2
  2d38-1 rolls two 38-sided die, and subtracts 1
  QUIT quits the program
    ''')
    while True:
        all_right=True
        user_input=input('> ').lower()
        if user_input=='quit':
            print('Thanks for playing!')
            exit()
        if 'd' in user_input:
            input_list=user_input.split('d')
            
            if input_list[0].isnumeric():
                dice_count=int(input_list[0])
                if '+' in input_list[1] or '-' in input_list[1]:
                    if '+' in input_list[1]:
                
                        foo=input_list[1].split('+')
                        if foo[0].isnumeric():
                            side_count=int(foo[0])
                            try:
                                bonus=int(foo[1])
                            except Exception as error:
                                all_right=False
                                print(INVALID_LINE)
                                print(f'Input was invalid because: {error}') 
                        else:
                            all_right=False
                            print(INVALID_LINE)
                            print('Input was invalid because: Missing the number of sides.') 
                    else:
                        
                        foo=input_list[1].split('-')
                        if foo[0].isnumeric():
                            side_count=int(foo[0])
                            try:
                                bonus=int(foo[1])
                            except Exception as error:
                                all_right=False
                                print(INVALID_LINE)
                                print(f'Input was invalid because: {error}') 
                        else:
                            all_right=False
                            print(INVALID_LINE)
                            print('Input was invalid because: Missing the number of sides.') 
                else:
                    if input_list[1].isnumeric():
                        side_count=int(input_list[1])
                        bonus=0
                    else:
                        all_right=False
                        print(INVALID_LINE)
                        print('Input was invalid because: Missing the number of sides.')
            else:
                all_right=False
                print(INVALID_LINE)
                print('Input was invalid because: Missing the number of dice.')    
        else:
            all_right=False
            print(INVALID_LINE)
            print('Input was invalid because: Missing the "d" character.')

        if all_right:
            if bonus==0:
                die_numbers=[random.randint(1,side_count) for d in range(dice_count)]
                die_numbers_str=[str(no) for no in die_numbers]
                print(f'Total: {sum(die_numbers)} (Each die: {", ".join(die_numbers_str)})')
            else:
                
                die_numbers=[random.randint(1,side_count) for d in range(dice_count)]
                die_numbers_str=[str(no) for no in die_numbers]
                if bonus>0:
                    die_numbers.append(bonus)
                    die_numbers_str.append(f'+{bonus}')
                    print(f'Total: {sum(die_numbers)} (Each die: {", ".join(die_numbers_str)})')
                else:
                    die_numbers.append(bonus)
                    die_numbers_str.append(f'-{bonus}')
                    print(f'Total: {sum(die_numbers)} (Each die: {", ".join(die_numbers_str)})')

if __name__=='__main__':
    main()