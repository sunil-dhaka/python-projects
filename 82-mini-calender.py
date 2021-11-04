# simple and short version of 8-get-calender.py
try:
    import datetime
except Exception as e:
    print(f'Error: {e}')
    exit()

WEEK=['Su','Mo','Tu','We','Th','Fr','Sa']
BOX_WIDTH=2
CAL_WIDTH=7*BOX_WIDTH+6
# 7*len(day)+6 (spaces between them)

def main():
    today=datetime.date.today()
    year=today.year
    month=today.month
    cal_text=today.strftime('%b %Y').center(CAL_WIDTH,' ')+'\n'
    for day in WEEK:
        cal_text+=day+' '

    # to add new-line
    cal_text+='\n'

    curr_date=datetime.date(year,month,1)

    while curr_date.weekday()!=6:
        curr_date-=datetime.timedelta(1)

    for i in range(5):
        for j in range(7):
            day=str(curr_date.day)
            if curr_date.month==month:
                if curr_date==today:
                    ''' 
                    link: https://stackoverflow.com/questions/5947742/how-to-change-the-output-color-of-echo-in-linux
                    for windows might not work; I did not check
                    to work on all OS can use a module like colorama or termcolor etc
                    '''
                    cal_text+=f"\033[1;32m{' '*(2-len(day))+day}\033[m"+' '
                else:
                    cal_text+=' '*(2-len(day))+day+' '
            else:
                cal_text+=' '*BOX_WIDTH + ' '
            curr_date+=datetime.timedelta(1)
        cal_text+='\n'
        
    print(cal_text)

if __name__=='__main__':
    main()