import re

fname = "regex_sum_38405.txt"
f = open(fname, "r")
ints = []
for line in f.readlines():
    numbers = re.findall('[0-9]+', line)
    for x in numbers:
        ints.append(int(x))
print (sum(ints))
