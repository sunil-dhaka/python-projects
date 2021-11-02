import random
import time

# style can be changed 
BAR_CHAR=chr(9608)

def main():
    print('Downloading file ...')
    curr_download_bytes=0
    total_download_bytes=4096
    tic=time.time()

    while curr_download_bytes<total_download_bytes:

        # download some bytes
        curr_download_bytes+=random.randint(0,1000)

        progress_string=progress_bar(curr_download_bytes,total_download_bytes)
        
        # since default end for print is new-line we specify end as ''

        print('\b'*(len(progress_string)+1),end='',flush=True)
        
        print(progress_string,end='',flush=True)
        for i in range(5):
            print('|',end='',flush=True)
            time.sleep(0.1)
            print('\b',end='',flush=True)
            print('\\',end='',flush=True)
            time.sleep(0.1)
            print('\b',end='',flush=True)
            print('-',end='',flush=True)
            time.sleep(0.1)
            print('\b',end='',flush=True)
            print('/',end='',flush=True)
            time.sleep(0.1)
            print('\b',end='',flush=True)
    
        # time.sleep(0.2)
        # print('\b'*(len(progress_string)+1),end='',flush=True) # this is an important step

    toc=time.time()
    # print('\n') 
    print('\b'*(len(progress_string)+1),end='\n',flush=True)

    print(f'Downloaded in {round(toc-tic)} seconds')


    
# returns a string 
def progress_bar(progress,total,bar_len=40):
    progress_string=""
    progress_string+="["

    # main bar progress
    # to make sure that progress is between 0 and total
    if progress>total:
        progress=total
    if progress<0:
        progress=0

    progress_bars=int((progress/total)*bar_len)
    # copy BAR_CHAR progress_bars many tiems
    progress_string+=BAR_CHAR*(progress_bars)
    # copy " " remainig length of 
    progress_string+=' '*(bar_len-progress_bars)

    # end bar progress

    progress_string+="] "

    # add download data
    download_percent=round(100*(progress/total))

    progress_string+=str(download_percent) + "%"

    progress_string+=" "
    progress_string+=str(progress)+"/"+str(total)+ "  "

    return progress_string

if __name__=='__main__':
    main()