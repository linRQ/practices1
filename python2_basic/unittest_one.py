import unittest, python2_basic.my_math as m


class ProductTestCase(unittest.TestCase):

    def testIntegers(self):
        for x in range(-10, 10):
            for y in range(-10, 10):
                p = m.product(x, y)
                self.assertTrue(p == x*y, 'Integer multiplication failed')

    def testFloats(self):
        for x in range(-10, 10):
            for y in range(-10, 10):
                x = x/10.0
                y = y/10.0
                p = m.product(x, y)
                self.assertTrue(p == x*y, 'Floats multiplication failed')


if __name__=='__main__':
    unittest.main()