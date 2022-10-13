from __future__ import print_function
from array import array
import cv2 as cv
import argparse
import numpy as np

parser = argparse.ArgumentParser(description='Code for Segmentation for Limiarizartion Threshold.')
parser.add_argument('--input', help='Path to input image.', default='veia.png')
args = parser.parse_args()
src = cv.imread(cv.samples.findFile(args.input))

if src is None:
    print('Could not open or find the image:', args.input)
    exit(0)

def generate_t(possible_threshold,table):

    positions_255 = []

    positions_0 = []

    for row in range(len(table)):
        for column in range(len(table[row])):
                if table[row][column] >= possible_threshold:
                    positions_255.append(table[row][column])
                else:
                    positions_0.append(table[row][column])

    mean_255 = np.mean(positions_255)

    mean_0 = np.mean(positions_0)

    new_threshold = (mean_255 + mean_0)/2

    return new_threshold

def generate_T(first_threshold,possible_threshold,table):

    new_threshold = generate_t(possible_threshold,table)

    if abs(first_threshold - new_threshold) <= 0.001:
        return new_threshold

    else:
        generate_T(first_threshold,new_threshold,table)

image = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

table_values = cv.split(image)[1]

max_value = np.max(table_values)

min_value = np.min(table_values)

first_threshold = (max_value + min_value)/2

the_threshold = generate_T(first_threshold,first_threshold,table_values)

for r in range(len(table_values)):
        for c in range(len(table_values[r])):
                if table_values[r][c] >= the_threshold:
                        table_values[r][c] = 255
                else:
                        table_values[r][c] = 0

print(table_values)









