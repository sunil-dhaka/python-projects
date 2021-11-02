import sys, time
import sevseg

timer_seconds_left=0
if len(sys.argv)>1:
    time_input=sys.argv[1].split(':')
    for i,t in enumerate(time_input):
        timer_seconds_left+=int(t)*(60)**(2-i)
else:
    print('Please give a input in formate 1:25:30. Demo for 30 Sec runs like this')
    timer_seconds_left=30
# print(timer_seconds_left)
try:
    while True:
        # although it makes it look like that digits are being overwritten but not in reality
        print('\n'*60)
        hours=timer_seconds_left//3600
        minutes=(timer_seconds_left-(hours*3600))//60
        seconds=(timer_seconds_left-(hours*3600)-(minutes*60))

        # print the time

        hours_top,hours_mid,hours_bot=sevseg.getSevSegStr(hours,2).splitlines()
        minutes_top,minutes_mid,minutes_bot=sevseg.getSevSegStr(minutes,2).splitlines()
        seconds_top,seconds_mid,seconds_bot=sevseg.getSevSegStr(seconds,2).splitlines()

        print(hours_top,' ',minutes_top,' ',seconds_top)
        print(hours_mid,'*',minutes_mid,'*',seconds_mid)
        print(hours_bot,'*',minutes_bot,'*',seconds_bot)
        print()
        print('Press Ctrl+C to quit.')

        if timer_seconds_left==0:
            print('*** BOOM ***')
            break
        
        time.sleep(1)

        '''print('\b'*(len(hours_top+minutes_top+seconds_top)+2*2),end='',flush=True)
        print('\b'*(len(hours_mid+minutes_mid+seconds_mid)+2*2),end='',flush=True)
        print('\b'*(len(hours_bot+minutes_bot+seconds_bot)+2*2),end='',flush=True)'''
        
        timer_seconds_left-=1
        
    
except:
    print(f'Countdown Stopped at {timer_seconds_left}')
    sys.exit()