# Local and Global
x = 10

def test():
    global x
    x = 23

print(x)
test()
print(x)
