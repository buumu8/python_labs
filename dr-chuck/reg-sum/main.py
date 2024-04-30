import re

f = open("regex_sum_1999988.txt")
text = f.read()
s = sum([int(x) for x in re.findall("([0-9]+)", text)])
print(f"sum= {s}")
