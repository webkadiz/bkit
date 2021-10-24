def print_result(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if type(res) == list: print(*res, sep='\n')
        elif type(res) == dict: [print(key, '=', value) for key, value in res.items()]
        else: print(res)

        return res

    return wrapper
