import unittest
import itertools
from main import *

class UnitTests(unittest.TestCase) :
    def test_more_of_equal(self) :
        for i in range(10) : 
            n = 0
            for d in data :
                if d>=i : n = n + 1
            self.assertTrue( numberGreaterThanOrEqualTo(data,i)==n, "Your function more_or_equal is not working" )
                
    def test_less_of_equal(self) :
        for i in range(10) : 
            n = 0
            for d in data :
                if d<=i : n = n + 1
            self.assertTrue( numberGreaterThanOrEqualTo(data,i)==n, "Your function less_or_equal is not working" )   
                
    def test_more_than(self) :
        for i in range(10) : 
            n = 0
            for d in data :
                if d>i : n = n + 1
            self.assertTrue( numberGreaterThanOrEqualTo(data,i)==n, "Your function more_than is not working" )
                
    def test_less_than(self) :
        for i in range(10) : 
            n = 0
            for d in data :
                if d<i : n = n + 1
            self.assertTrue( numberGreaterThanOrEqualTo(data,i)==n, "Your function less_than is not working" )               
