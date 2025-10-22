# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z). 
# Определите максимальное количество идущих подряд символов, 
# среди которых каждая из букв UVWXYZ встречается не более ста раз.

#5
f = open('24_5.txt').readline()

e = 0
m = 0
k = {x:0 for x in 'UVWXYZ'}

for r in range(len(f)):
    if f[r] in 'UVWXYZ': k[f[r]]+=1
    while any(k[x]>100 for x in 'UVWXYZ'):
        if f[e] in 'UVWXYZ': k[f[e]]-=1
        e+=1
    m =max(m, r-e+1)
print(m)
#2844
