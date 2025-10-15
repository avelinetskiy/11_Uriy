def f(a, b, c):
    if a<b or c=='11': return 0
    if a==b: return 1
    if a == 20:
        c+='1'
    if a== 8:
        c+='1'
    return f(a-1, b, c)+f(a-3, b, c)+f(a//2, b, c)

print(f(31, 3, ''))