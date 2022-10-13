import argparse
import cv2
import numpy as np

op = 0
table_valeus = 0
arr_seg = []

def click_image(event, x, y, flags, param):
    while      

    


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
clone = image.copy()
cv2.namedWindow("image")

print('1 - Conectividade 4')
print('2 - Conectividade 8')
print('3 - Conectividade M')
op = str(input('Escolha uma das opções de conectividade:'))
while op!='1' and op!='2'and op!='3':
    print('Opção Invalida')    
    print('1 - Conectividade 4')
    print('2 - Conectividade 8')
    print('3 - Conectividade M')
    op = str(input('Escolha apenas uma das opções de conectividade:'))

table_valeus = cv2.split(image)[1]
cv2.setMouseCallback("image", click_image)