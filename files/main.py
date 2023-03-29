files = []
i=0

for i in range(1, 10001):
    files.insert(i - 1, open(str(i), "w"))
    files[i - 1].write(str(i))
    files[i - 1].close()