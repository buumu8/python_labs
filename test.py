count = 0

for i in range(1000):
    if i % 101 == 7:
        count += 1
        print(i)

print(count)
