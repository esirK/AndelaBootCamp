import unittest
from generate_primes import primes_generator

class TestPrimeNumbers(unittest.TestCase):
    def test_a_prime(self):
        self.assertEqual(primes_generator(5),(2,3,5))

    def test_not_stings(self):
        self.assertEqual(primes_generator('five'),'Not A Prime Number')

    def test_not_negative(self):
        self.assertEqual(primes_generator(-5),'A is Non Negative')

    def test_minimum_prime_number(self):
        self.assertEqual(primes_generator(1),'Not A Prime Number')

    def test_not_list(self):
        self.assertEqual(primes_generator([2]),'Not A prime Number')

    
if __name__=='__main__':
    unittest.main()
