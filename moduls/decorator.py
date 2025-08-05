def add_seporator(f):
    def inner(*args, **kwargs):
        print('-' * 20, '*' * 3, '-' * 20)
        result = f(*args, **kwargs)
        print('-' * 20, '*' * 3, '-' * 20)
        return result
    return inner