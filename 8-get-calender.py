try:
    import datetime
except Exception as e:
    print(f'Error: {e}')
    exit()

CAL_WIDTH=len('+----------+----------+----------+----------+----------+----------+----------+')
BOX_WIDTH=10

WEEK=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
MONTHS=['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']

def main():
    while True:
        print('Which year?')
        year=input('> ')

        if year.isnumeric() and int(year)>0 and int(year)<9999:
            break
        print('Please give a num between 0 and 10000.')
    
    while True:
        print(f'Which month of the {year}?')
        month=input('> ')

        if month.isnumeric() and int(month)>0 and int(month)<13:
            break
        print('Please give a number in 1-12')
    cal_text=get_calender(year,month)

    print(cal_text)

    with open(f'calender_{year}_{month}.txt','w') as cal:

        cal.write('\n'.join(cal_text.split('\n')))

    print(f'Calender saved as >>> calender_{year}_{month}.txt')
    
def get_calender(year,month):
    year=int(year)
    month=int(month)

    #upper setup for calender
    cal_line=''
    cal_line+=(MONTHS[month-1] + ' ' + str(year)).center(CAL_WIDTH,' ')+'\n'
    cal_line+='...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..\n'

    curr_date=datetime.date(year,month,1)

    # just takes back until we reach last sunday date

    while curr_date.weekday()!=6:
        curr_date-=datetime.timedelta(1)
        # print(curr_date.day)

    # then we start from last sunday and make a five week calender irrespective of the month
    # it can be modified to check wether we need fifth month or not for some cases but why bother
    # and make code more complicated, almost always we will need five weeks

    for i in range(5):
        cal_line+='+----------+----------+----------+----------+----------+----------+----------+\n'

        for j in range(7):
            day=curr_date.day
            curr_date+=datetime.timedelta(1)
            cal_line+='|'+' '*2+'\b'*len(str(day))+str(day)+' '*(BOX_WIDTH-2)
        cal_line+='|\n'
        
        for k in range(3):
            for j in range(7):
                cal_line+='|'+' '*BOX_WIDTH
            cal_line+='|\n'

    # bottom cover line for calender
    cal_line+='+----------+----------+----------+----------+----------+----------+----------+\n'

    return cal_line
if __name__=='__main__':
    main()
