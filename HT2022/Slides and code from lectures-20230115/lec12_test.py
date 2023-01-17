#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import lec12

class TestBinarySearch(unittest.TestCase):
    
    # names of methods should begin with "test_"
    def test_1(self):
        l = [1,3,4,8,10,20,30,40,90,100,101,102]
        for i in range(len(l)):
            self.assertEqual(lec12.binary_search(l,l[i]), i)
            
    def test_2(self):
        l = []
        self.assertRaises(ValueError, lambda: lec12.binary_search(l,1))


if __name__ == '__main__':
    unittest.main()

# python hypothesis library helps with generating inputs to test

