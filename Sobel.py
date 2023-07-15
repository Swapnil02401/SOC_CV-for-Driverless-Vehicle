import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('lane.jpg')
lane_image = np.copy(img)

gray = cv.cvtColor(lane_image, cv.COLOR_RGB2GRAY)
image_blurred = cv.GaussianBlur(gray, (5, 5), 0)

sobel_x = cv.Sobel(image_blurred, cv.CV_64F, 1, 0, ksize=3)
sobel_y = cv.Sobel(image_blurred, cv.CV_64F, 0, 1, ksize=3)

# Convert the gradient images to absolute values
sobel_x = np.abs(sobel_x)
sobel_y = np.abs(sobel_y)

sobel_combined = cv.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)

sobel_normalized = cv.normalize(sobel_combined, None, 0, 255, cv.NORM_MINMAX, cv.CV_8U)

#cv.imshow('gray',blur) 
#cv.imshow('Lane',img)  
cv.imshow('Canny',sobel_normalized)

plt.imshow(sobel_normalized)
plt.show()

def region_of_interest(image):
      height = image.shape[0]
      polygons = np.array([
      [(0,370), (575, 380), (290, 225)]
      ])
      mask = np.zeros_like(image)
      cv.fillPoly(mask, polygons, 255)
      masked_image = cv.bitwise_and(image, mask)
      return masked_image
	

  
cropped_image = region_of_interest(sobel_normalized) #changing it to show ROI instead of canny image.
cv.imshow('result', cropped_image)

def display_lines(image, lines):
    line_image = np.zeros_like(image)
    if lines is not None:
        for x1, y1, x2, y2 in lines:
            cv.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 10)
    return line_image

def make_coordinates(image, line_parameters):
    slope, intercept = line_parameters
    y1 = image.shape[0]
    y2 = int(y1*(3/5))
    x1 = int((y1 - intercept)/slope)
    x2 = int((y2 - intercept)/slope)
    return np.array([x1, y1, x2, y2])

def average_slope_intercept(image, lines):
    left_fit = []
    right_fit = []
    for line in lines:
        x1, y1, x2, y2 = line.reshape(4)
        parameters = np.polyfit((x1, x2), (y1, y2), 1)
        slope = parameters[0]
        intercept = parameters[1]
        if slope < 0:
            left_fit.append((slope, intercept))
        else:
            right_fit.append((slope, intercept))
    left_fit_average = np.average(left_fit, axis=0)
    right_fit_average = np.average(right_fit, axis=0)
    left_line = make_coordinates(image, left_fit_average)
    right_line = make_coordinates(image, right_fit_average)
    return np.array([left_line, right_line])

lines = cv.HoughLinesP(cropped_image, 2, np.pi/180, 100, np.array([]), minLineLength=40, maxLineGap=5)  #conversion of c = -mx + c tp xcos% - ysin% + rho = 0 , np.array is the accumulator array and 100 is the min number of votes req

averaged_lines = average_slope_intercept(cropped_image, lines)

line_image = display_lines(cropped_image,averaged_lines)

combo_image = cv.addWeighted(cropped_image, 0.8, line_image, 1, 1)

cv.imshow('result', combo_image)

cv.waitKey(0)