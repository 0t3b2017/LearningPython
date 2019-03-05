def outer():
    test = 1 # outer scope

    def inner():
        nonlocal test
        test = 2 # nearest enclosing scope
        print('inner:', test)
    inner()
    print('outer:', test)

test = 0
outer()
print('global:', test)
