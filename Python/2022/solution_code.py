def f(x, d, a):
    if d <= x:
        c= 0
        while x % d == 0:
            c+= 1
            x //= d
        a(c, end=" ")
        f(x, d+1, a)
#f(120, 2, print)

#? again, some of the variables are useless and made just to make it harder to read. Cleaner code would look like this:

def f2(x, d):
    if d <= x:
        c = 0
        while x % d == 0:
            c += 1
            x //= d
        print(c, end=" ")
        f2(x, d+1)
f2(120, 2)

#? now its much cleaner and we can see that proffesor wanted to hide that "a" was just a synonym for print in this case.  
#? in every function run we are checking how many times we can divide a number and then do the same but divider+1
#? 120 -> 60 -> 30 -> 15/2 = 7,5, so we can divide 3 times, then 15 -> 5/3 = 2,5 so 1 time, 5/4  = 1,... so 0 times, 5/5 its 1 time
#* and here the program ends
#! the output will be 3 1 0 1