import unittest

from binarySearch import binarySearchUpper

class binarySearchTest(unittest.TestCase):
    def test_01(self):
        alist = [1, 3, 6, 10, 15]
        item = 1

        itemIndexFound = binarySearchUpper(alist, item)

        self.assertEqual(itemIndexFound, 0)

    def test_02(self):
        alist = [1, 3, 6, 10, 15]
        item = 3

        itemIndexFound = binarySearchUpper(alist, item)

        self.assertEqual(itemIndexFound, 1)

    def test_03(self):
        alist = [1, 3, 6, 10, 15]
        item = 5

        itemIndexFound = binarySearchUpper(alist, item)

        self.assertEqual(itemIndexFound, 2)

    def test_04(self):
        alist = [1, 3, 6, 10, 15]
        item = 2

        itemIndexFound = binarySearchUpper(alist, item)

        self.assertEqual(itemIndexFound, 1)

    def test_05(self):
        alist = [1, 3, 6, 10, 15]
        item = 20

        itemIndexFound = binarySearchUpper(alist, item)

        self.assertEqual(itemIndexFound, -1)

if __name__ == '__main__':
    unittest.main()