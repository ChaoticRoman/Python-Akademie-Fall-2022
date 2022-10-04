def f(value):
    if value:
        print(value, "True")
    else:
        print(value, "False")


f("")
f("a")
f([])
f([[]])
f(-1)
f(f)
