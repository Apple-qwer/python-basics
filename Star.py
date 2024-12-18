n = 5 
y = 0
for i in range(1,6):
    print ('*' * i + ' ' * (n - i) + ' ' * (n - i) + '*' * i) 
    i += 1
for i in range(1,6):
    print (('*' * n + ' ' * y) + (' ' * y + '*' * n)) 
    n -= 1
    y += 1