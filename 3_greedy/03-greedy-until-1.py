import time

n, k = map(int, input().split())

result = 0
timetest = time.time()
while True :

    if(n == 1) :
        break

    if(n % k == 0) :
        n = n / k
        result += 1
        continue
    else :
        n -= 1
        result += 1
        continue
timeresult = time.time()
print("time : ", str((timeresult - timetest)), "s")
print(result)