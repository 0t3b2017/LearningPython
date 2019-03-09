x = [1, 2, 3]
def func(x):
    x[1] = 42
    print('function1:', x)
    x = 'something else'
    print('function2:', x)
print('global1:', x)
func(x) 
print('global:2', x)
