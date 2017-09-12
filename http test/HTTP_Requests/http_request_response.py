import itertools
i=0
combo = itertools.permutations("abcdefghijklmnopopqrstuvwxyz1234567890",8)

for x in combo:
    print ''.join(x)
    i+=1
    if i == 10:
        break

