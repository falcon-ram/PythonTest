import csv
from collections import defaultdict, Counter

with open('data/survey_results_public.csv', encoding='utf-8') as f:
    csv_reader = csv.DictReader(f)

    # Solution 1: using counters
    # yes_count = 0
    # no_count = 0
    # for line in csv_reader:
    #     if line['Hobbyist'] == 'Yes':
    #         yes_count += 1
    #     elif line['Hobbyist'] == 'No':
    #         no_count +=1
    
    # Solution 2: using a dictionary
    # counts = {
    #     'Yes' : 0,
    #     'No': 0
    # }

    # Solution 3: using a default dictionary instead of initializing the dict ourselves
    # counts = defaultdict(int)

    # Solution 4: using a default Counter class
    counts = Counter()

    for line in csv_reader:
        counts[line['Hobbyist']] += 1


#total = yes_count + no_count
total = counts['Yes'] + counts['No']

#yes_pct = (yes_count/total) * 100
yes_pct = (counts['Yes'] / total) * 100
yes_pct = round(yes_pct, 2)

#no_pct = (no_count/total) * 100
no_pct = (counts['No'] / total) * 100
no_pct = round(no_pct, 2)

print(f'Yes: {yes_pct}%')
print(f'No:  {no_pct}%')


        
        