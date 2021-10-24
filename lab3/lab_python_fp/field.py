def field(items, *args):
    assert len(args) > 0

    for item in items:
        d = {arg: item.get(arg) for arg in args if item.get(arg)}
        
        if len(d) == 0: continue

        if len(args) == 1: yield d[args[0]]
        else: yield d
