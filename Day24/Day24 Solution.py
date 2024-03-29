class Solution:
    def nthPoint(self, n):
        modulo = 10 ** 9 + 7
        
        fib = [0] * (n + 1) 
        fib[0] = 1
        fib[1] = 1
        
        for i in range(2, n + 1):
            fib[i] = (fib[i - 1] + fib[i - 2]) % modulo
        return fib[n]