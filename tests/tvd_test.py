import unittest
import cv2
import numpy as np
from image_helper import image_open, local_path
from tvd import TotalVariationDenoising
from numpy.testing import assert_array_equal, assert_almost_equal

image = image_open(local_path('../assets/example.bmp'))
image = cv2.cvtColor(image, cv2.COLOR_BGR2YCR_CB)
subject = TotalVariationDenoising(image[:, :, 0])
output = image_open(local_path('../assets/example_tv.bmp'))
output = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)


class TotalVariationDenoisingTest(unittest.TestCase):
  def test_rectangular_tv(self):
    mat = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]], np.float32)
    I = cv2.cvtColor(mat, cv2.COLOR_GRAY2BGR)
    I = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)
    output = np.array([[6.4981, 6.4981, 6.4981], [6.4992, 6.4992, 6.4992], [6.5008, 6.5008, 6.5008], [6.5019, 6.5019, 6.5019]], np.float32)
    subject = TotalVariationDenoising(I)
    result = subject.generate()
    assert_almost_equal(result, output, decimal=4)

  def test_mini_tv(self):
    mat = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], np.float32)
    I = cv2.cvtColor(mat, cv2.COLOR_GRAY2BGR)
    I = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)
    output = np.ones((3, 3, 3)) * 5
    subject = TotalVariationDenoising(I)
    result = subject.generate()
    assert_almost_equal(result, output[:, :, 0], decimal=6)

  def test_left(self):
    result = subject.left(10)
    assert_array_equal(result, np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 9]))

  def test_right(self):
    result = subject.right(10)
    assert_array_equal(result, np.array([0, 0, 1, 2, 3, 4, 5, 6, 7, 8]))
