import unittest
import twisted.trial.unittest

import gens_simple
import gens_twisted


class SimpleGeneratorsTestCase(unittest.TestCase):

    def test_generators(self):
        self.assertItemsEqual(list(gens_simple.good_generator()), [True])
        with self.assertRaises(ValueError):
            gens_simple.bad_function()
        with self.assertRaises(ValueError):
            list(gens_simple.bad_generator())


class TwistedGeneratorsTestCase(twisted.trial.unittest.TestCase):

    def test_generators(self):
        # Should not throw an error
        gens_twisted.good_generator()
        self.assertFailure(gens_twisted.bad_generator(), ValueError)


if __name__ == '__main__':
    unittest.main()
