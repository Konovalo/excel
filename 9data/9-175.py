# Автор: А. Рогов

import csv

reader = csv.reader(open('9-170.csv'), delimiter=';')
k = 0
for line in reader:
    line = [int(i) for i in line]
    double = {i for i in line if line.count(i) > 1}
    single = [i for i in line if line.count(i) == 1]
    if len(double) == 1 and \
            len(single) == 4 and\
            min(single) + max(single) <= double.pop() * 2:
        k += 1
print(k)
