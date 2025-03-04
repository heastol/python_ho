import sys
args = sys.argv
i = int(args[1][:-1])
j = int(args[2])
for i in range(i, i + j):
    print('=====%d단=====' %i)
    for k in range(1, 10):
        print(f'{i} X {k} = {i * k}')
        