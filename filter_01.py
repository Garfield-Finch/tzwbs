a = []
infile = open("B090512020.txt", "r")
for i in infile:
    a.append(i)
infile.close()

a = a[2:]
for i in range(len(a)):
    a[i] = eval(a[i][:-1])


ct = []
flt = []
for i in range(20):
    counter = 0
    pre = a[i*1000+200]
    peak = False
    for j in range(i*1000+200+1, i*1000+300):
        if a[j] >= a[j-1]:
            peak = True
        elif peak:
            counter += 1
            peak = False
        pre = a[j]
    ct.append(counter)
    if counter >= 40:
        flt.append(False)
    else:
        flt.append(True)
print(flt)
