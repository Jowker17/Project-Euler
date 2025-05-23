# Finding Longest Collatz Chain
import time
f1 = time.perf_counter()
from dataclasses import dataclass
@dataclass
class Chain:
    value: int
    length: int
memo = {1:0,2:1}
def getChain(n,memo):
    N = n
    steps = 0
    while n!=1 and n not in memo:
        if n%2==0:
            n=n//2
        else:
            n=3*n+1
        steps+=1
    length = steps+memo[n] # or memo.get(n,0) if n not in memo gets 0
    memo[N] = length
    return Chain(value=N,length=length)
maxchain = Chain(value=0,length=0)
for i in range(3,10**6,2):
    chain = getChain(i,memo)
    if chain.length > maxchain.length:
        maxchain = chain
print("Longest Chain: ",maxchain.length)
print("Number: ",maxchain.value)
print("execution time : ",time.perf_counter()-f1) # 2.4 ms  That's achievement for Python
