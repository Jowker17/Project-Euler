#Finding 10001th Prime Number
def is_prime(x):
    if sum(list(map(int,str(x))))%3==0:
        return False
    if x < 2 or x % 2 ==0:
        return False
    if x == 2:
        return True
    for i in range(3, int(x ** 0.5) + 1, 2):
        if x % i == 0:
            return False
    return True
import time
f1=time.perf_counter()
count = 2
i = 3
while count != 10001:
    i += 2
    if is_prime(i):
        count += 1
print("10001th Prime: ",i) # Prime Number: 104743
print("Execution time: ",time.perf_counter()-f1) # Execution time: 1.53377 ms
