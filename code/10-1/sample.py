import unittest

def abs(n):
	if n < 0:
		return -n

	return n


class ABSTestCase(unittest.TestCase):
    """ Test for the Query """ 

    def test_abs(self):
        self.assertEqual(abs(7), 7)
        self.assertEqual(abs(0), 0)
        self.assertEqual(abs(-3), 3)


unittest.main()