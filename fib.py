



def fib(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    result = fib(n-2) + fib(n-1)
    return result
    
import timeit


def fib_aux(n, memo):
    if n in memo:
        return memo[n]
    result = fib_aux(n-2,memo) + fib_aux(n-1, memo)
    memo[n] = result
    return result

def fib_db(n):
    memo = dict()
    memo[0] = 0
    memo[1] = 1
    return fib_aux(n, memo)
    




# setup = '''
# def fib(n):
#     if n == 1:
#         return 1
#     if n == 0:
#         return 0
#     result = n + fib(n-1)
#     return result

# def fib_db(n):
#     memo = dict()
#     memo[0] = 0
#     memo[1] = 1
#     return fib_aux(n, memo)
    

# def fib_aux(n, memo):
#     if n in memo:
#         return memo[n]
#     result = n + fib_aux(n-1, memo)
#     memo[n] = result
#     return result
# '''

# code = '''
# fib_db(900)
# '''

print(fib_db(8))