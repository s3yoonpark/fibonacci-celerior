import time, sys 

class Number: 
    def __init__(self, a, m, b): 
        self.a = a 
        self.m = m 
        self.b = b 
        # self = a + m * sqrt(b) 
    def __str__(self): 
        return f"{self.a} {self.m} {self.b}"
    def __add__(self, other): 
        return Number(self.a + other.a, self.m + other.m, self.b) 
    def __sub__(self, other): 
        return Number(self.a - other.a, self.m - other.m, self.b) 
    def __mul__(self, other): 
        return Number(self.a * other.a + self.m * other.m * self.b, self.a * other.m + other.a * self.m, self.b) 
    
    def __pow__(self, e): 
        if e == 0: 
            return Number(1, 0, 5)  
        if e % 2 == 1: 
            x = self ** (e // 2)
            return x * x * self 
        if e % 2 == 0: 
            x = self ** (e // 2)
            return x * x 

def pow(n, e): 
    if e == 0: 
        return 1
    if e % 2 == 1: 
        x = pow(n, e//2) 
        return x * x * n
    if e % 2 == 0: 
        x = pow(n, e//2) 
        return x * x 

def old_fib(n): 
    t1 = time.time() 
    if n <= 2: 
        return 1
    table = [1, 1, 0] 
    for i in range(2, n):
        table[(i+3)%3] = table[(i+2)%3] + table[(i+1)%3]
    print("time taken for old fibonacci : ", time.time() - t1)
    return table[(n+2)%3]

def new_fib(n): 
    t1 = time.time() 
    a = Number(1, 1, 5) 
    r = (a ** n).m * 2
    # r = (a ** n - b ** n).m
    x = pow(2, n) 
    print("time taken for new fibonacci : ", time.time() - t1)
    return r // x 

if __name__ == "__main__": 
    sys.set_int_max_str_digits(0)
    n = int(input())
    # old_fib(n) 
    new_fib(n)

    