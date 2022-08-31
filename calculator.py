def add(*num):
    sumz = 0
    for n in num:
        sumz += n
    print(sumz)

def subtract(*nums):
    sumz = 0
    for n in nums:
        sumz -= n
    print(sumz)

def divide(num, *num2):
    product = 0
    product += num
    for n in num2:
        product = product/n
    print(product)

def multiply(num, *num2):
    product = 0
    product += num
    for n in num2:
        prodcut = product * n
    print(product)

print("type:\nadd(...) for addition\nsubtract()

