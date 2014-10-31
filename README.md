py-tvd
======

This is a Python implementation of [Total Variation Denoising](http://visl.technion.ac.il/~gilboa/PDE-filt/tv_denoising.html) method proposed by Guy Gilboa.
>Reduces the total-variation of the image. Filters out noise while preserving edges. Textures and fine-scale details are also removed.


Requirements
------------------
To run this code you need the following packages:

* [Python 2.7](https://www.python.org/download/releases/2.7/)
* [OpenCV](http://opencv.org/)
* [Numpy](http://www.numpy.org/)
* [numexpr](https://github.com/pydata/numexpr)

Maybe it should work also on other version of python, but it's untested.

**Everything but OpenCV can be installed via `pip install -r requirements`**

Installation
-----------------
To install everything just run:

```shell
python setup.py install
```

Maybe you have to run it with `sudo`.

Testing
-----------------
Test are provided via [`unittest`](https://docs.python.org/2/library/unittest.html).

To run them all:

```shell
nosetests
```

Examples
-----------------

```python
import cv2
from tvd import TotalVariationDenoising
import os

image = cv2.imread(os.path.dirname(__file__) + '/../assets/example.bmp')
image = cv2.cvtColor(image, cv2.COLOR_BGR2YCR_CB)
subject = TotalVariationDenoising(image[:, :, 0])
output = subject.generate()
cv2.imshow('Total Variation Denoising image', output / 255)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

The conversion to *YCbCr* color space is optionally (sure?)

Final Notes
-----------------
This library is already in development, so don't use it for __real__ purposes.
