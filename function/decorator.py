def log(text):
    print('1')
    def decorator(func):
        print('2')
        def wrapper(*args, **kw):
            print('3')
            print('%s %s():' % (text, func.__name__))
            print('fucntion starting')
            f = func(*args, **kw)
            print('fucntion ending')
            return f
        print('4')
        return wrapper
    print('5')
    return decorator

@log('execute')
def now():
    print('now is 11/18')
    return 

f1 = now
f1()