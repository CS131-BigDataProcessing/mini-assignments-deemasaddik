#!/bin/bash

python3 <<EOF

from math import power, divide
import unittest
class TestMathFunction(unittest.TestCase):

  def test_power(self):
      self.assertEqual(power(-2,3), -8)
      self.assertEqual(power(3,-2), 1/9)
      self.assertEqual(power(3,0), 1)
      self.assertEqual(power(0,19999), 0)
      self.assertEqual(power(9,2),81)
      self.assertEqual(power(9,1/2), 3)
      self.assertEqual(power(1/9,1/2), 1/3)

  def test_divide(self):
    self.assertEqual(divide(-2,8), -0.25)
    self.assertEqual(divide(-2,-8), 0.25)
    self.assertEqual(divide(2,-8), -0.25)
    self.assertEqual(divide(50,10), 5)
    self.assertEqual(divide(0,8), 0)
    with self.assertRaises(ZeroDivisionError):
        divide(8, 0)

if __name__ == '__main__':  #  Python scripts are importable as modules or standalone
      unittest.main()
EOF

