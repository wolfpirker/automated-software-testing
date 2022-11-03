def multiply(*args):
    print(args)
    total = 1
    for args in args:
        total = total * args
    return total

print(multiply(1, 3, 5))

def add(x, y):
    return x + y

nums = [3, 5]
print(add(*nums))

def apply(*args, operator):
    if operator == "*":
        # Note: we want to pass in the tuple as
        # single elements, so we have to use star!
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "no valid operator provided to apply()"

print(apply(1, 3, 6, 7, operator="*"))