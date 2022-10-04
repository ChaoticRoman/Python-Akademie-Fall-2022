a = [5]

def f():
    print(a[0])
    a[0] = 4
    print(a[0])

f()
print(a[0])
