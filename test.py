import family_friday as test_doc
from unittest.mock import patch
import unittest

class TestRandomize(unittest.TestCase):
    """Tests the randomize function."""
    def test_01_empty_array(self):
        array = []
        expected = []
        res = test_doc.randomize(array)
        self.assertEqual(expected, res)

    def test_02_small_array(self):
        """A test for if an array is smaller than 4 and does not get
        def test_02_small_array(self):
        split into sublists."""
        array = [1,2]
        expected = [1,2]
        res = test_doc.randomize(array)
        self.assertEqual(expected, res)

    def test_03_multiple_lists(self):
        for i in range(4, 26):
            array = [j for j in range(i)]
            valid = True
            res_mod = test_doc.randomize(array)
            for group in res_mod:
                if 3 > len(group) or len(group) > 5:
                    valid = False
            self.assertTrue(valid)

class TestInsert(unittest.TestCase):
    """Test the insert function. The file 'test.txt' contains five employees."""
    def setUp(self):
        # setup to revert the test file back to normal
        self.array_orig = test_doc.load('test.txt').copy()

    def tearDown(self):
        # to make sure we don't increase our test data too much
        test_doc.store(self.array_orig, 'test.txt')

    def test_05_correct_output_ins(self):
        array = test_doc.load('test.txt')
        res = test_doc.insert('Alonzo', array, 'test.txt')
        self.assertEqual(res, '6')

    def test_06_correct_array_ins(self):
        array = test_doc.load('test.txt')
        res = test_doc.insert('Alonzo', array, 'test.txt')
        self.assertEqual(array, test_doc.load('test.txt'))

class TestDelete(unittest.TestCase):
    """Test the delete function. The file 'test.txt' contains five employees."""
    def setUp(self):
        # setup to revert the test file back to normal
        self.array_orig = test_doc.load('test.txt').copy()

    def tearDown(self):
        # to make sure we don't increase our test data too much
        test_doc.store(self.array_orig, 'test.txt')

    def test_07_correct_output_del(self):
        array = test_doc.load('test.txt')
        res = test_doc.delete('Tim', array, 'test.txt')
        self.assertEqual(res, '4')

    def test_08_correct_array_del(self):
        array = test_doc.load('test.txt')
        res = test_doc.delete('Tim', array, 'test.txt')
        self.assertEqual(array, test_doc.load('test.txt'))

    def test_09_not_an_employee(self):
        array = test_doc.load('test.txt')
        res = test_doc.delete('Alonzo', array, 'test.txt')
        self.assertFalse(res)

if __name__ == '__main__':
    unittest.main()
