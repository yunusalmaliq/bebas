y = 0
n = 1
x = 0
fib = []
fib.insert(y,1)
batas = input("Masukkan batas: ")

while y != batas:
        while n != 3:
                y = y + 1
                fib.insert(y,(fib[y-n] + fib[y-n]))
                n = n + 1
        fib.insert(y,(fib[y-(n-1)] + fib[y-(n-2)]))
        y = y + 1

print '---------------'
print 'DERET FIBONACCI'
print '---------------'
while x != batas:
        print fib[x]
        x = x + 1