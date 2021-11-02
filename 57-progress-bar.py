import random
import time

# style can be changed 
BAR_CHAR=chr(9608)

def main():
    print('Downloading file ...')
    curr_download_bytes=0
    total_download_bytes=4096
    while curr_download_bytes<total_download_bytes:

        # download some bytes
        curr_download_bytes+=random.randint(0,500)

        progress_string=progress_bar(curr_download_bytes,total_download_bytes)
        
        # since default end for print is new-line we specify end as ''
        print(progress_string,end='',flush=True)
        time.sleep(0.5)
        print('\b'*len(progress_string),end='',flush=True)


    
# returns a string 
def progress_bar(progress,total,bar_len=30):
    progress_string=""
    progress_string+="["

    # main bar progress
    # to make sure that progress is between 0 and 1
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
    download_percent=round(100*(progress/total),1)

    progress_string+=str(download_percent) + "%"

    progress_string+=" "
    progress_string+=str(progress)+"/"+str(total)

    return progress_string

if __name__=='__main__':
    main()