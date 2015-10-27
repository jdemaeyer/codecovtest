def good_generator():
    yield True


def bad_generator():
    yield bad_function()


def bad_function():
    raise ValueError
