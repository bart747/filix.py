#!/usr/bin/env python3.6

import filix
import unittest
import os
import time

class TestCollectMethod(unittest.TestCase):
    
    def test_collection_uniqueness(self):
        list_test = [1, 2, 3]
        filix.collect(2, list_test)
        self.assertEqual(list_test, [1, 2, 3])

    def test_collection_adding(self):
        list_test = [7, 2, 1]
        filix.collect(99, list_test)
        self.assertEqual(list_test, [7, 2, 1, 99])

class TestSelectByTagsMethod(unittest.TestCase):

    def test_select_by_tags(self):
        coll = []
        test_file_path_a = 'test_file_testa.txt'
        test_file_path_b = 'test_file_testb.txt'
        test_file_path_c = '.test_file_testb.txt' # dot-files aren't allowed 
        open(test_file_path_a, 'a').close()
        open(test_file_path_b, 'a').close()
        open(test_file_path_c, 'a').close()
        filix.select_by_tags(['testb', 'teSTa'], coll) # should ignore case 
        time.sleep(0.001)
        os.remove(test_file_path_a)
        os.remove(test_file_path_b)
        os.remove(test_file_path_c)
        self.assertEqual(coll, ['test_file_testb.txt', 'test_file_testa.txt'])


if __name__ == '__main__':
    unittest.main()