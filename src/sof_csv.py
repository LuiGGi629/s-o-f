import csv
import datetime
import os
from collections import defaultdict, Counter

os.chdir('/Users/wojtek/PycharmProjects/s-o-f/')

with open('data/survey_results_public.csv') as f:
    t0 = datetime.datetime.now()
    csv_reader = csv.DictReader(f)
    dev_type_info = {}

    for line in csv_reader:
        dev_types = line['DevType'].split(';')

        for dev_type in dev_types:
            dev_type_info.setdefault(dev_type, {
                'total': 0,
                'language_counter': Counter()
            })
            languages = line['LanguageWorkedWith'].split(';')
            dev_type_info[dev_type]['language_counter'].update(languages)
            dev_type_info[dev_type]['total'] += 1

print()
print('The 5 most popular languages for each developer type:')
print()
for dev_type, info in dev_type_info.items():
    print(dev_type)

    for language, value in info['language_counter'].most_common(5):
        language_pct = (value / info['total']) * 100
        print(f"\t{language}: {language_pct:.2f}%")

dt = datetime.datetime.now() - t0
print('---------------------------------------------------------------------------------------------------------------')
print(f"Done, total time: {dt.total_seconds():.2f} sec.", flush=True)
