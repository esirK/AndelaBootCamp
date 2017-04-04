import unittest
from generate_primes import primes_generator

class TestPrimeNumbers(unittest.TestCase):
    def test_a_prime(self):
        self.assertEqual(primes_generator(5),[2,3,5])
if __name__=='__main__':
    unittest.main()
