f = open('26_5.txt').readlines()[1:]
n = f[0]
a = sorted([int(x) for x in f[1:]])[::-1]
k = 0
r = 0

while len(a)>1:
    if a[0] - a[1] >= 9:
        k+=1
        r = a[1]
        a.remove(a[0])
        a.remove(a[1])
    else:
        a.remove(a[1])
print(k, r)