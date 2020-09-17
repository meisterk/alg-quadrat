import unittest

# Function quadrat:
# Parameter: number
# Result: quadrat of number


def quadrat(number):
    return number * number


# Testcases
class TestQuadrat(unittest.TestCase):
    def test_quadrat_2_is_4(self):
        self.assertEqual(quadrat(2), 4)

    def test_quadrat_5_is_25(self):
        self.assertEqual(quadrat(5), 25)

    def test_quadrat_minus_2_is_4(self):
        self.assertEqual(quadrat(-2), 4)

    def test_quadrat_0_is_0(self):
        self.assertEqual(quadrat(0), 0)


# Run Tests
if __name__ == "__main__":
    unittest.main()
