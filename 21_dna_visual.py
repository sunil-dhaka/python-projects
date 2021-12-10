import random, sys, time

DNA_STR=[('G','C'),('C','G'),('T','A'),('A','T')]

PAUSE=0.1
DNA_ROWS=[
    '       ##',
    '      #{}-{}#',
    '     #{}---{}#',
    '    #{}-----{}#',
    '   #{}------{}#',
    '  #{}------{}#',
    '  #{}-----{}#',
    '   #{}---{}#',
    '    #{}-{}#',
    '     ##',
    '    #{}-{}#',
    '   #{}---{}#',
    '  #{}-----{}#',
    '  #{}------{}#',
    '   #{}------{}#',
    '    #{}-----{}#',
    '     #{}---{}#',
    '      #{}-{}#',
]

def main():
    print('press ctrl-c to stop\n')
    time.sleep(2)
    row_count=0
    while True:
        # get a random sequence
        dna_seq=random.choice(DNA_STR)
        row_count+=1
        if row_count == len(DNA_ROWS):
            row_count=0

        # handle `##` case
        if row_count==0 or row_count==9:
            print(DNA_ROWS[row_count])
            continue
        
        print(DNA_ROWS[row_count].format(dna_seq[0],dna_seq[1]))
        sys.stdout.flush()
        time.sleep(PAUSE)

if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()