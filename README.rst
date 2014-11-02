py-tvd
======

This is a Python implementation of `Total Variation Denoising`_ method
proposed by Guy Gilboa. >Reduces the total-variation of the image.
Filters out noise while preserving edges. Textures and fine-scale
details are also removed.

Requirements
------------

To run this code you need the following packages:

-  `Python 2.7`_
-  `OpenCV`_
-  `Numpy`_
-  `numexpr`_

Maybe it should work also on other version of python, but it’s untested.

**Everything but OpenCV can be installed via
``pip install -r requirements``**

Installation
------------

To install everything just run:

.. code:: shell

    python setup.py install

Maybe you have to run it with ``sudo``.

Testing
-------

Test are provided via ```unittest```_.

To run them all:

.. code:: shell

    nosetests

Examples
--------

.. code:: python

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

The conversion to *YCbCr* color space is optionally (sure?)

Final Notes
-----------

This library is already in development, so don’t use it for **real**
purposes.

.. _Total Variation Denoising: http://visl.technion.ac.il/~gilboa/PDE-filt/tv_denoising.html
.. _Python 2.7: https://www.python.org/download/releases/2.7/
.. _OpenCV: http://opencv.org/
.. _Numpy: http://www.numpy.org/
.. _numexpr: https://github.com/pydata/numexpr
.. _``unittest``: https://docs.python.org/2/library/unittest.html
