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

def old_fib(n): 
    t1 = time.time() 
    table = [1, 1] 
    while len(table) != n: 
        table.append(table[-1] + table[-2]) 
    print("time taken for old fibonacci : ", time.time() - t1)
    return table[n-1]

def new_fib(n): 
    t1 = time.time() 

    a = Number(1, 1, 5) 
    b = Number(1, -1, 5) 
    r = (a ** n - b ** n).m
    x = (Number(2, 0, 5) ** n).a

    print("time taken for new fibonacci : ", time.time() - t1)
    return r // x 

if __name__ == "__main__": 
    sys.set_int_max_str_digits(0)
    n = int(input())
    print(old_fib(n))
    print(new_fib(n))

    