import re
rfile = open("regex_sum_2479175.txt")
total = 0
for line in rfile:
    line = line.rstrip()
    x = re.findall('[0-9]+', line)
    if len(x) > 0:
        for num in x:
            total += int(num)
print(total)