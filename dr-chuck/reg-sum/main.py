import re

f = open("regex_sum_1999988.txt")
s = 0
for line in f:
    line = line.rstrip()
    list = re.findall("([0-9]+)", line)
    s += sum([int(l) for l in list])
print(f"sum= {s}")
