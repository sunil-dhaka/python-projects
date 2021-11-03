import datetime,random

print('no of birthdays to generate?')
BIRTHDAY_COUNT=int(input())


def main():
    print(f'Here are {BIRTHDAY_COUNT} random birthdays:')
    random_bds=bd_generator()
    print(', '.join(random_bds['bds']))
    if random_bds['same-count']>0:
        print(f'Here we have {random_bds["same-count"]} common BDs on: ',', '.join(random_bds['same-bds']))
    else:
        print('Here we have NO common bds')
    # how to check if Enter is pressed?        
    input('Press enter for to run birthday simulations(default is 10,000)')
    
    s=input('Specify number or Leave blank for default\n')
    if s=='':
        sim_counts=10000
    else:
        if s.isalpha():
            print('Give valid simulation number. An integer as high as you can think')
            exit()
        else:
            sim_counts=int(s)
    
    print(f'Running {sim_counts} simulations ...')
    match_count=bd_simulator(sim_counts)
    probability = round(match_count / sim_counts * 100, 2) 
    print(f'Out of {sim_counts} simulations of', BIRTHDAY_COUNT, 'people, there was a') 
    print('matching birthday in that group', match_count, 'times. This means') 
    print('that', BIRTHDAY_COUNT, 'people have a', probability, '% chance of') 
    print('having a matching birthday in their group.') 
    print('That\'s probably more than you would think!')


    

def bd_generator(bd_count=BIRTHDAY_COUNT):
    start_date=datetime.date(2020,1,1)
    end_date=datetime.date(2020,12,31)
    in_between_time=end_date-start_date
    in_between_days=in_between_time.days

    random_bds=[]
    same_count=0
    same_bds=[]
    for i in range(bd_count):
        new_bd=random.randint(1,in_between_days)
        if new_bd in random_bds:
            same_count+=1
            same_bds.append(new_bd)
        random_bds.append(new_bd)

    same_bd_dates=[str((start_date + datetime.timedelta(bd)).strftime('%d %b')) for bd in same_bds]
    bd_dates=[str((start_date + datetime.timedelta(bd)).strftime('%d %b')) for bd in random_bds]
    
    return {'same-count':same_count,'bds':bd_dates,'same-bds':same_bd_dates}
    
def bd_simulator(sim_counts,bd_count=BIRTHDAY_COUNT):
    start_date=datetime.date(2020,1,1)
    end_date=datetime.date(2020,12,31)
    in_between_time=end_date-start_date
    in_between_days=in_between_time.days

    same_counts=0
    for j in range(sim_counts):
        random_bds=[]
        for i in range(bd_count):
            new_bd=random.randint(1,in_between_days)
            if new_bd in random_bds:
                same_counts+=1
                break
            random_bds.append(new_bd)

    return same_counts

if __name__=='__main__':
    main()

'''
The Birthday Paradox shows us that in a group of N people, the odds 
that two of them have matching birthdays is surprisingly large. 
This program does a Monte Carlo simulation (that is, repeated random 
simulations) to explore this concept. 
(It's not actually a paradox, it's just a surprising result.)
'''