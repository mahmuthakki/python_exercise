def my_sum(*args):
    sum=0
    
    for arg in args:
        sum+=arg
    return sum

print(my_sum(1,2,3))