for i in range(5):
    n = 0
    if i != 1: n += 1
    if i == 3: n += 1
    if i == 4: n += 1
    if i != 4: n += 1
    if n == 3: print(64 + i)


# i     n
# 0     2
# 1     1
# 2     1+1
# 3     1+1+1     67
# 4     1+1
