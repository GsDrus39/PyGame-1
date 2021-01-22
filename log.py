def logging(function):
    def decorated_function(*args, **kwargs):
        try:
            a = function(*args, **kwargs)
        except Exception:
            print(function.__name__, 'in:', (*args, kwargs), 'out: EXCEPTION', Exception)
        else:
            print(function.__name__, 'in:', (*args, kwargs), 'return: ', a)
        return a
    return decorated_function