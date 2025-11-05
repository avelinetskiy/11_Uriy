# def f(x, a):
#     return (a%9==0) and (280%x==0) <= ( (not(a%x==0))<=(not(730%x==0)) )

# n = 0

# for a in range(1, 1001):
#     fl=0
#     for x in range(1, 10000):
#         if not f(x, a):
#             fl=1
#             break
#     if fl == 0:
#         n+=1
# print(n)

# def f(x, y, a):
#     return (x-2*y<3*a) or (2*y>x) or (3*x>50)

# for a in range(1, 1000):
#     fl = 0
#     for x in range(1, 1000):
#         if fl == 1:
#                 break
#         for y in range(1, 1000):
#             if not f(x, y, a):
#                 fl = 1
#                 break
#     if fl == 0:
#         print(a)
#         break

# def f(x, a):
#     return x&51 == 0 or ((x&41 == 0) <= (x&a == 0))

# for a in range(1000, 1, -1):
#     fl = 0
#     for x in range(1, 1000):
#         if not f(x, a):
#             fl = 1
#             break
#     if fl == 0:
#         print(a)
#         break

# p = [x for x in range(10,30)]
# q = [x for x in range(13,19)]
# a = [x for x in range(10,30)]
# for x in range(1,100):
#     if not(((x in a) <= (x in p)) or (x in q)):
#         a.remove(x)
# print(a)

# P = [i for i in range(25, 51)]
# Q = [i for i in range(32, 48)]
# m = 0
# for Amin in range(0, 60):
#     for Amax in range(Amin + 1, 60):
#         check = 1
#         A = [i for i in range(Amin, Amax)]
#         for x in range(0, 101):
#             f = ((not(x in A)) <= (x in P)) <= ((x in A) <= (x in Q))
#             if not f:
#                 check = 0
#                 break
#         if check == 1:
#             m = max(m,Amax - Amin)
# print(m - 1)