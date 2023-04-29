def power_module(x, y, z):
    res = 1
    while y > 0:
        if y & 1:
            res *= x
        y >>= 1
        x *= x
    
        print("x:", x, "y:", y, "res:", res)
    return res

print("++++++++++++++++")
power_module(3,4,3)
print("-----------------")
power_module(3,6,3)
