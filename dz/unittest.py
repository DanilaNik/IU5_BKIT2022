from unittest import TestCase, main
from generator import fib
import time

class fib_test(TestCase):
    
    def test__fib_1(self):
        arr = [i for i in fib(10)]
        true_arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        self.assertEqual(arr, true_arr)

    def test_fib_2(self):
        arr = [i for i in fib(0)]
        true_arr = []
        self.assertEqual(arr, true_arr)

    def test_fib_3(self):
        arr = [i for i in fib(1)]
        true_arr = [0]
        self.assertEqual(arr, true_arr)
        
    def test_time_fib_1(self): #lazy evaluation
        begin = time.time()
        a = fib(1000000)
        end = time.time() - begin
        self.assertLess(end, 1) 

    def test_time_fib_2(self): #calculation on demand      
        begin = time.time()
        a = [i for i in fib(1000000)] 
        end = time.time() - begin
        self.assertLess(1, end)  
   

if __name__ == '__main__':
    main()
