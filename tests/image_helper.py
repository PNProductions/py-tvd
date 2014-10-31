import cv2
import os.path
from numpy import clip, copy, float64


def local_path(path):
  return os.path.dirname(__file__) + '/' + path


def image_open(filename, mode=None):
  if os.path.isfile(filename):
    if mode is None:
      image = cv2.imread(filename)
    else:
      image = cv2.imread(filename, mode)
    if image is None:
      IOError('Unable to open image file: ' + filename)
    else:
      return image
  else:
    raise IOError('Image file not found at: ' + filename)

def to_matlab_ycbcr(image):
  # http://stackoverflow.com/questions/26078281/why-luma-parameter-differs-in-opencv-and-matlab
  return clip(16 + (219 / 255.0) * image, 16, 235)


def from_matlab_ycbcr(image):
  # http://stackoverflow.com/questions/26078281/why-luma-parameter-differs-in-opencv-and-matlab
  # return clip(image * (255 / 219.0) - 16, 0, 255)
  return clip(image * (255 / 219.0) - 16, 0, 255)


def get_matlab_luma(image):
  image = image.astype(float64)
  image = copy(image)
  image[:, :, 2] = image[:, :, 2] * 0.114
  image[:, :, 1] = image[:, :, 1] * 0.587
  image[:, :, 0] = image[:, :, 0] * 0.299
  image = image.sum(axis=2)
  return image
