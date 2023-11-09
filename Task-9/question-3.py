# 3. Using the python lambda function create a fibonacci series from 1 to 50 elements?
# fibonacci series - group of numbers beginning with 0 and 1 in which each number is the sum of the two before it. It begins 0, 1, 1, 2, 3, 5, 8, 13, 21 and continues infinitely.

n = 10
fib = [0,1] # fibonacci series - starts with 0 and 1

list(map(lambda i:fib.append(fib[-2]+fib[-1]),range(2,n)))
print(fib)