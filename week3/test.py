# 3.201 Test driven approach

import unittest
import numpy as np

class MyTest (unittest.TestCase):

  def test_mean(self):
    mean = np.mean([1, 2, 3])
    self.assertEqual(mean, 2)

  def test_mean2(self):
    mean = np.mean([1, 1, 1])
    self.assertEqual(mean, 2)

unittest.main()
