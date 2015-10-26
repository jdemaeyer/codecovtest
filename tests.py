import unittest


def good_generator():
    yield True


def bad_generator():
    yield bad_function()


def bad_function():
    raise ValueError


class GeneratorTestCase(unittest.TestCase):

    def test_generators(self):
        self.assertItemsEqual(list(good_generator()), [True])
        with self.assertRaises(ValueError):
            bad_function()
        with self.assertRaises(ValueError):
            list(bad_generator())
