import factor as fc

num1 = int(input("what is the first num?:"))

num2 = int(input("what is the second num?:"))

def gcf(a, b):
    gcf_ls = []

    ls1 = fc.factors(a)
    ls2 = fc.factors(b)

    for i in ls1:
        if i in ls2:
            gcf_ls.append(i)
    
    return gcf_ls[-1]

print(gcf(num1, num2))
