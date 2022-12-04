import itertools


def create_Iterator():
    some_dict = {"a": 1, "b": 2, "c": 3}

    for key in some_dict:
        print(key)

    dict_iterator = iter(some_dict)
    print("dict_iterator: ", dict_iterator)
    print(list(dict_iterator))


def squares(n=10):
    print(f"Generating squres from 1 to {n**2}")
    for i in range(1, n + 1):
        yield i**2


def create_Generator():
    gen = squares()
    for x in gen:
        print(x, end=" ")


def _make_gen():
    for x in range(100):
        yield x**2


def expression_Generator():
    gen = (x**2 for x in range(100))
    print(sum(gen))

    dict_gen = ((i, i**2) for i in range(5))
    print(dict(dict_gen))


def p_itertools():
    first_letter = lambda x: x[0]

    names = ["Alan", "Adam", "Wes", "Will", "Albert", "Steven"]

    for letter, names in itertools.groupby(names, first_letter):
        print(letter, list(names))
