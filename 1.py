for x in range(35000000, 40000001):
    a = []
    for i in range(1, int(x**0.5)+1):
        if x%i == 0:
            if i%2!=0:
                a.append(i)
            if (x//i)%2!=0:
                a.append(x//i)
            if len(set(a))>5:
                break
    if len(set(a))==5:
        print(x)