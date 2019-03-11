def func(a=[], b={}):
    print(a)
    print(b)
    print('#' * 18)
    a.append(len(a)) # affect a's default value
    b[len(a)] = len(a) # affeect b's default value

func()
func()
func()
func()
