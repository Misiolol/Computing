
def f(n, k, g):
    if n > 2:
        return f(n-k, k, g) + f(n-g(1,1,g), k, g)
    else: 
        return 2

#? g argument is basicly useless in this code so i removed it lmao, also value of f(1,1,g) will be always 2 so i replaced it as well

def f2(n, k):
    if n > 2:
        return f2(n-k, k) + f2(n-2, k)
    else:
        return 2

#? now in the edited code it is easier to see that basicly, every time we are digging deeper into recursion by subtracting k or 2 from given n 
#? then we are checking if n is <= 2 if it is we return 2 as the value, co basicly aour task is to count how much time te recursion will happen 


print(f2(5, 1))


#! output will be 10 from both finctions :D

