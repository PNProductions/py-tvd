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
