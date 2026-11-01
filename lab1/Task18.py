import time

def log_calls(filename):
    def decorator(func):
        def wrapper(*args):
            with open(filename, 'a') as f:
                f.write(f'{time.ctime()}\t{func.__name__}\t{", ".join(map(str, args))}\n')
            return func(*args)
        return wrapper
    return decorator

@log_calls('text.txt')
def function(word):
    print(word)

function('Python')
function('vibe')