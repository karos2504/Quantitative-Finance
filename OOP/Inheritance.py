class Dad():
    say_hello = ('Hello')

class Son(Dad):
    say_world = ('World')

son = Son()
print(son.say_hello)
print(son.say_world)