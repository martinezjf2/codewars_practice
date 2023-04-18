# Starter Code

def sum_mul(n, m):
    pass

# Final Code

def sum_mul(n, m):
    sumu = 0
    if n > 0 and m > 0:
        for i in range(n, m):
            if (i % n == 0):
                sumu += i
    else:
        return 'INVALID'
    return sumu

# or

def sum_mul(n, m):
    L=[]
    if n<=0 or m<=0:
        return 'INVALID'
    else:
        for i in range(0,m):
            if i*n<m:
                L.append(i*n)
        return sum(L)

# or 

def sum_mul(n, m):
    result = 0
    if n <= 0 or m <= 0:
        return 'INVALID'
    for i in range(n, m):
        if i % n == 0:
            result += i    
               
    return result

# Link to CodeWars: https://www.codewars.com/kata/sum-of-multiples