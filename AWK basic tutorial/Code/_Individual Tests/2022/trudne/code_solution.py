def f(x, d, a):
    if d <= x:
        c= 0
    while x % d == 0:   
        c+= 1
        x //= d
    a(c, end=" ")
f(120, 2, print)


#? the difference is in missing recursion, the code will run only once printing number 3
