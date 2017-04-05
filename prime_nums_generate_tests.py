import unittest
from generate_primes import primes_generator

class TestPrimeNumbers(unittest.TestCase):
    def test_a_prime(self):
        self.assertEqual(primes_generator(5),[2,3,5])

    def test_not_stings(self):
        self.assertEqual(primes_generator('five'),'Not A Prime Number')

    def test_not_negative(self):
        self.assertEqual(primes_generator(-5),'Not A Prime Number')

    def test_minimum_prime_number(self):
        self.assertEqual(primes_generator(1),'Not A Prime Number')

    def test_not_list(self):
        self.assertEqual(primes_generator([2]),'Not A prime Number')
    def test_does_not_include_non_primes(self):
        self.assertNotIn([0,1,4,6],primes_generator(6))
    def test_return_value_is_list(self):
        self.assertTrue(isinstance(primes_generator(10), list), msg="The function should return a list")

    
if __name__=='__main__':
    unittest.main()
