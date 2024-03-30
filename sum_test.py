def MySum(n):
    run_sum = 0
    for i in range(1,n+1):
        run_sum += i**2+1
    return run_sum

a = int(input("how much?:"))

b = MySum(a)

print(b)