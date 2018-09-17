from itertools import groupby

ds = [1,1,2,3,3,4,4,8,8]
keys = []
groups = []

for k,g in groupby(ds):
    keys.append(k)
    groups.append(list(g))

# keys (unique elements)
print('keys ',keys)
