def my_function():
    #test = 1 # local scope
    print('my_function:', test)

test = 0 # global scope
my_function()
print('global:', test)
