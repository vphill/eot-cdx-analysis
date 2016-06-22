from __future__ import print_function, division
import sys
from collections import Counter

if len(sys.argv) != 3:
    print('usage: compare_count_lists_for_change.py <eot2008 list> <eot2012 list>')
    exit()

eot2008_size = 160212141
eot2012_size = 194066940

with open(sys.argv[1]) as fp:
    eot2008_list = fp.readlines()

with open(sys.argv[2]) as fp:
    eot2012_list = fp.readlines()

eot2008_list = [d.strip() for d in eot2008_list]
eot2012_list = [d.strip() for d in eot2012_list]


eot2008_count_dict = mydict = {k: int(v) for k, v in (a.split('\t') for a in eot2008_list)}

eot2012_count_dict = mydict = {k: int(v) for k, v in (a.split('\t') for a in eot2012_list)}

eot_2008_set = set(eot2008_count_dict.keys())
eot_2012_set = set(eot2012_count_dict.keys())

print('Unique in 2008: {}'.format(len(eot_2008_set)))
print('Unique in 2012: {}'.format(len(eot_2012_set)))

common_count = eot_2008_set & eot_2012_set
print('Common Between Both: {}'.format(len(common_count)))

eot_2008_only = eot_2008_set - eot_2012_set
print('Only in 2008: {}'.format(len(eot_2008_only)))

eot_2012_only = eot_2012_set - eot_2008_set
print('Only in 2012: {}'.format(len(eot_2012_only)))

eot_2008_only_count_dict = {}
for i in eot_2008_only:
    eot_2008_only_count_dict[i] = eot2008_count_dict[i]

eot_2012_only_count_dict = {}
for i in eot_2012_only:
    eot_2012_only_count_dict[i] = eot2012_count_dict[i]

eot_2008_ten_uniq = Counter(eot_2008_only_count_dict).most_common(30)
eot_2012_ten_uniq = Counter(eot_2012_only_count_dict).most_common(30)

print('\neot2008_only_top_thirty')
for i in eot_2008_ten_uniq:
    print('{}\t{}'.format(i[0], i[1]))

print('\neot2012_only_top_thirty')
for i in eot_2012_ten_uniq:
    print('{}\t{}'.format(i[0], i[1]))

print('\nShared values sorted by biggest change')
change_list = []
for item in common_count:
    e08 = eot2008_count_dict[item]
    e12 = eot2012_count_dict[item]
    change_number =  e12 - e08

    change_perc = (e12 - e08) / e08

    change_list.append((item, e08, e12, change_number, abs(change_number), change_perc))

for k in sorted(change_list, key=lambda x: x[4], reverse=True):
    print('\t'.join([str(s) for s in k]))

