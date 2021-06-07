import unittest

from main import Rational_num, periodToDecimal


class TestMethods(unittest.TestCase):


    def test_format(self):
        with self.assertRaises(IOError):
            Rational_num(1.1, 1)
        with self.assertRaises(IOError):
            Rational_num(1, 0)
        with self.assertRaises(IOError):
            Rational_num(0, 0)

    def test_addiction(self):
        self.assertEqual(Rational_num(1, 1) + Rational_num(1, 1), Rational_num(2, 1))
        self.assertEqual(Rational_num(-1, 1) + Rational_num(1, 1), Rational_num(0, 1))
        self.assertEqual(Rational_num(1, -1) + Rational_num(1, 1), Rational_num(0, 1))
        self.assertEqual(Rational_num(-1, 1) + Rational_num(1, -1), Rational_num(-2, 1))
        self.assertEqual(Rational_num(0, 1) + Rational_num(0, 1), Rational_num(0, 1))

    def test_subtraction(self):
        self.assertEqual(Rational_num(1, 1) - Rational_num(1, 1), Rational_num(0, 1))
        self.assertEqual(Rational_num(-1, 1) - Rational_num(1, 1), Rational_num(-2, 1))
        self.assertEqual(Rational_num(1, -1) - Rational_num(1, 1), Rational_num(-2, 1))
        self.assertEqual(Rational_num(1, 1) - Rational_num(1, -1), Rational_num(2, 1))
        self.assertEqual(Rational_num(0, 1) - Rational_num(1, 1), Rational_num(-1, 1))

    def test_multiplicatoin(self):
        self.assertEqual(Rational_num(1, 1) * Rational_num(1, 1), Rational_num(1, 1))
        self.assertEqual(Rational_num(1, 1) * Rational_num(2, 1), Rational_num(2, 1))
        self.assertEqual(Rational_num(-1, 1) * Rational_num(-2, 1), Rational_num(2, 1))
        self.assertEqual(Rational_num(0, 1) * Rational_num(2, 1), Rational_num(0, 3))

    def test_truedivision(self):
        self.assertEqual(Rational_num(1, 1) / Rational_num(1, 1), Rational_num(1, 1))
        self.assertEqual(Rational_num(2, 1) / Rational_num(-2, 1), Rational_num(-2, 2))
        with self.assertRaises(ZeroDivisionError):
            Rational_num(5, 1) / Rational_num(0, 1)

    def test_floordivision(self):
        self.assertEqual(Rational_num(1, 1) // Rational_num(1, 1), 1)
        self.assertEqual(Rational_num(1, 1) // Rational_num(-1, 1), -1)
        with self.assertRaises(ZeroDivisionError):
            Rational_num(1, 1) // Rational_num(0, 1)

    def test_mod(self):
        self.assertEqual(Rational_num(1, 1) % Rational_num(1, 1), 0)
        self.assertEqual(Rational_num(3, 2) % Rational_num(1, 3), 1)
        self.assertEqual(Rational_num(3, 2) % Rational_num(1, -3), -1)
        with self.assertRaises(ZeroDivisionError):
            Rational_num(1, 1) % Rational_num(0, 1)

    def tests_comparison(self):
        self.assertTrue(Rational_num(2, 2) == Rational_num(1, 1))
        self.assertTrue(Rational_num(2, 2) != Rational_num(2, 1))
        self.assertTrue(Rational_num(1, 1) <= Rational_num(2, 2))
        self.assertTrue(Rational_num(2, 2) >= Rational_num(1, 2))
        self.assertTrue(Rational_num(3, 2) > Rational_num(1, 3))
        self.assertTrue(Rational_num(1, 3) < Rational_num(3, 2))

    def test_reduc1(self):
        a = Rational_num(2, 2)
        a.reduction()
        self.assertEqual(a, Rational_num(1, 1))

    def test_reduc2(self):
        a = Rational_num(0, 1)
        a.reduction()
        self.assertEqual(a, Rational_num(0, 1))

    def test_reduc3(self):
        a = Rational_num(3, 2)
        a.reduction()
        self.assertEqual(a, Rational_num(3, 2))

    def test_decimal(self):
        self.assertEqual(Rational_num(122, 99).decimalToPeriod(), "1.(23)")
        self.assertEqual(Rational_num(37, 300).decimalToPeriod(), "0.12(3)")
        self.assertEqual(Rational_num(1, 3).decimalToPeriod(), "0.(3)")
        self.assertEqual(Rational_num(1, -3).decimalToPeriod(), "-0.(3)")
        self.assertEqual(Rational_num(-1, 1).decimalToPeriod(), "-1.0")
        self.assertEqual(Rational_num(0, 1).decimalToPeriod(), "0.0")
        with self.assertRaises(IOError):
            Rational_num(36, 0).decimalToPeriod()

    def test_period(self):
        self.assertEqual(periodToDecimal("1.(23)"), Rational_num(122, 99))
        self.assertEqual(periodToDecimal("0.(3)"), Rational_num(1, 3))
        self.assertEqual(periodToDecimal("-0.(3)"), Rational_num(1, -3))
        self.assertEqual(periodToDecimal("-1.0"), Rational_num(-5, 5))
        self.assertEqual(periodToDecimal("0.0"), Rational_num(0, 1))


if __name__ == '__main__':
    unittest.main()
