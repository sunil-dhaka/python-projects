import time,sys

print('Press Ctrl + C to stop the clock')
try:
    while True:
        print(time.strftime('%H:%M:%S'),end='',flush=True)
        time.sleep(1)
        print('\b'*8,end='',flush=True)
except:
    print()
    print('Clock stopped')
    sys.exit()