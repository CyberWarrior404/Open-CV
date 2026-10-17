import cv2
import numpy as np

image1 = cv2.imread('girrraf.jpeg')
cv2.imshow('Giraffe', image1)
cv2.waitKey(0)
cv2.destroyAllWindows()

image2 = cv2.imread('what.jpeg')
cv2.imshow('What', image2)
cv2.waitKey(0)
cv2.destroyAllWindows()

gaussian_image=cv2.GaussianBlur(image1, (15, 15), 0)
cv2.imshow('Gaussian Blurred Giraffe', gaussian_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

image1 = cv2.imread('girrraf.jpeg')
cv2.imshow('Giraffe', image1)
cv2.waitKey(0)
cv2.destroyAllWindows()

median_image=cv2.medianBlur(image1, 5)
cv2.imshow('Median Blurred Giraffe', median_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

image1 = cv2.imread('girrraf.jpeg')
cv2.imshow('Giraffe', image1)
cv2.waitKey(0)
cv2.destroyAllWindows()

bilateral_image=cv2.bilateralFilter(image1, 31, 350, 350)
cv2.imshow('Bilateral Blurred Giraffe', bilateral_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

image1 = cv2.imread('girrraf.jpeg')
cv2.imshow('Giraffe', image1)
cv2.waitKey(0)
cv2.destroyAllWindows()


solid_border=cv2.copyMakeBorder(image1, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=(0, 255, 0))
cv2.imshow('Solid Border Giraffe', solid_border)
cv2.waitKey(0)
cv2.destroyAllWindows()

image2 = cv2.imread('what.jpeg')
cv2.imshow('What', image2)
cv2.waitKey(0)
cv2.destroyAllWindows()

reflective_border=cv2.copyMakeBorder(image2, 350, 350, 350, 350, cv2.BORDER_REFLECT, value=(0, 255, 0))
cv2.imshow('Reflective Border What', reflective_border)
cv2.waitKey(0)
cv2.destroyAllWindows()