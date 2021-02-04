import numpy as np
import cv2
from matplotlib import pyplot as plt

def calculateSSD(arr1,arr2):
    sub = list(np.array(arr1) - np.array(arr2))
    result = np.square(sub)
    return sum(result)
def calculateSAD(arr1,arr2):
    sub = list(np.array(arr1) - np.array(arr2))
    result = np.abs(sub)
    return sum(result)
def getwindow(row,col,windowsize,img):
    row = int(row - (windowsize/2))
    col = int(col - (windowsize/2))
    # print("the row value in window" + str(row) + "and the col value in window" + str(col))
    if row < 0 or col < 0:
        print("A7oo")
        return
    window = []
    i = 0
    j = 0
    for i in range(windowsize):
        for j in range(windowsize):
            window.append(img[row+i][col+j])
    return window
def dispWindowisOne(minimumSSD,pixel_coordinates ,disparity,left_shape ,left_img,right_img):
    for rows in range(left_shape[0]):
        print(rows)
        for cols in range(left_shape[1] - 31):
            pixel_value = left_img[rows][cols]
            pixel_coordinates[0] = 0
            pixel_coordinates[1] = 0
            minimumSSD = float('inf')
            for cols_dash in range(31):
                # print(cols_dash + cols)
                pixel_value_dash = right_img[rows][cols_dash + cols]
                if np.power(int(pixel_value) - int(pixel_value_dash), 2) < minimumSSD:
                    minimumSSD = np.power(int(pixel_value) - int(pixel_value_dash), 2)
                    pixel_coordinates[0] = rows
                    pixel_coordinates[1] = cols_dash + cols
                if cols_dash == 30 and pixel_coordinates[1] == 0:
                    # print()
                    pixel_coordinates[0] = rows
                    pixel_coordinates[1] = cols_dash + cols
                    break
            print("the row disparity saved at " + str(rows) + "and the cols  " + str(
                cols) + "and disparity value equal " + str(255 - (pixel_coordinates[1] - cols)))
            disparity[rows][cols] = (pixel_coordinates[1] - cols)
            print(disparity[rows][cols])
    return disparity
def disparitywithwindow(minimumSSD,pixel_coordinates ,disparity,left_shape,left_img,right_img,window_size ):
    for (rows) in range(left_shape[0]-window_size):
        print(rows + int(window_size/2))
        for cols in range(left_shape[1] - 31 - window_size): #left_shape[1] - 31 - window_size
            left_window_array = getwindow(rows + int(window_size/2) ,cols + int(window_size/2) ,window_size,left_img)
            print("Coodrinates")
            print("rows = "+ str(rows + int(window_size/2)))
            print("cols = " + str((cols + int(window_size/2))))
            print(left_window_array)
            print(left_img[rows + int(window_size/2)][cols + int(window_size/2)])
            # left_sad = sum_distinct_pairs(left_window_array)
            minimumSSD = float('inf')
            for cols_dash in range(31):
                right_window_array = getwindow(rows + int(window_size/2),cols_dash + cols + int(window_size/2) ,window_size,right_img)
                # right_sad = sum_distinct_pairs(right_window_array)
                # print("SAD VALUE" + str(np.power(int(left_sad) - int(right_sad), 2)))
                if calculateSAD(left_window_array,right_window_array) < minimumSSD:
                    # print("Found")
                    minimumSSD = calculateSAD(left_window_array,right_window_array)
                    pixel_coordinates[0] = rows + int(window_size/2)
                    pixel_coordinates[1] = cols_dash + cols + int(window_size/2)
                if cols_dash == 30 and pixel_coordinates[1] == 0:
                    pixel_coordinates[0] = rows
                    pixel_coordinates[1] = cols_dash + cols + int(window_size/2)
                    break
            # print("the row disparity found at " + str(pixel_coordinates[0]) + "and the cols  " + str(
            #     pixel_coordinates[1]) + "and disparity value equal " + str(255 - (pixel_coordinates[1] - (cols + int(window_size/2)) )))
            disparity[rows][cols] = (pixel_coordinates[1] - (cols + int(window_size/2)))
            # print(disparity[rows][cols])
    return disparity

left_img = cv2.cvtColor(cv2.imread('scene_l.jpg'), cv2.COLOR_BGR2GRAY)
left_shape = left_img.shape

right_img = cv2.cvtColor(cv2.imread('scene_r.jpg'), cv2.COLOR_BGR2GRAY)
right_shape = right_img.shape

minimumSSD = float('inf')
pixel_coordinates = [0 , 0]
disparity = np.zeros((left_shape[0], left_shape[1]))
disparity = disparitywithwindow(minimumSSD,pixel_coordinates ,disparity,left_shape,left_img,right_img,9 )

print(right_shape)
print(left_shape)

#Saving the disparity matrix
# a_file = open("d9-SAD.txt", "w")
# for row in disparity:
#     np.savetxt(a_file, row)
# a_file.close()

#Loading the disparity
#
# disparity = np.loadtxt("d9-SSD.txt").reshape(1,110592)
# for i in range(len(disparity)):
#     disparity[i] = 255 - disparity[i]
# disparity = disparity.reshape((left_shape[0], left_shape[1]))

plt.imshow(disparity,'gray')
plt.show()