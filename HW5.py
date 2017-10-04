import re

fname = "regex_sum_38405.txt"
f = open(fname, "r")
numbers = []
for line in f.readlines():
    nums = re.findall('[0-9]+', line)
    for x in nums:
        numbers.append(int(x))
print (sum(numbers))
