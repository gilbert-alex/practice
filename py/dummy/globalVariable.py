# dummy for global variables and scope

my_global = 5

def func1():
    global my_global
    my_global = 42

def func2():
    print(my_global)

func1()
func2()