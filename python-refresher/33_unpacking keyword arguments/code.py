def named(**kwargs):
    print(kwargs)


def print_nicely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")

print_nicely(name="Bob", age=26)

named(name="Bob", age=25)

details = {"name": "Bob", "age": 25}
named(**details)


