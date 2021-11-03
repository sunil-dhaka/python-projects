BITMAP = """
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
...................................................................."""

import sys,time
'''
takes a multi-line bitmap with ' ' indicated as noman's land  
'''
def bit_print(bitmap):
    print('Enter message to display using bit-map. Use uppercase for first char of each word')
    message=input("> ")

    # modify message to exclude spaces
    message=''.join(message.split(' '))
    massage_bitmap=[]

    bit_lines=bitmap.splitlines()

    message_bitmap=[]
    for line in bit_lines:
        for c in line:
            message_bitmap.append(c)
        message_bitmap.append('\n')

    bitmap_len=len(message_bitmap)

    curr_pos=0

    while(curr_pos<bitmap_len):

        curr_letter=0
        while(curr_letter<len(message)):
            if curr_pos>=bitmap_len:
                break
            if (message_bitmap[curr_pos]!=' ') and (message_bitmap[curr_pos]!='\n'):
                message_bitmap[curr_pos]=message[curr_letter]
                curr_letter+=1
            curr_pos+=1
    try:
        
        
        
        while True:
            print('\nPress Ctrl-C to stop.\n')
            print(''.join(message_bitmap))
            time.sleep(2)
    except:
        sys.exit()

if __name__=='__main__':
    bit_print(BITMAP)