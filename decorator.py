import functools
def log(arg):
    if isinstance(arg,str):    
        def decorator(func):
            #防止自己的__name__属性被更改
            @functools.wraps(func)
            def wrapper(*args,**kw):
                print(func.__name__+'-->begin call')
                #这种写法表示func(*args,**kw),print(func.__name__+'-->end call')都会执行，并只返回第一个的执行结果,
                #return func(*args,**kw),print(func.__name__+'-->end call') 返回两个函数的执行结果
                return [func(*args,**kw),print(func.__name__+'-->end call')][0]
            return wrapper
        return decorator
    else:
        func=arg
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print(func.__name__+'-->begin call')
            return [func(*args,**kw),print(func.__name__+'-->end call')][0]
        return wrapper

@log('ex')
def f():
    return 1
print(f())
print(f.__name__)

@log
def a():
    print(3)
a()
print(a.__name__)