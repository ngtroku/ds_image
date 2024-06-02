import cv2
import numpy as np

def show_diff(image_jpg, image_png):
    png, jpg = cv2.imread(image_png), cv2.imread(image_jpg)
    png_array, jpg_array=np.array(png), np.array(jpg)
    png_array16, jpg_array16 = png_array.astype(np.int16), jpg_array.astype(np.int16)
    diff=abs(png_array16-jpg_array16)
    diff_normal=(255*diff)/diff.max()
    diff_array=diff_normal.astype(np.uint8)
    return diff_array

if __name__ == '__main__':
    image_jpg, image_png = "./example4.jpg", "./example4.png"
    is_save = True
    diff = show_diff(image_jpg, image_png)

    # save result
    if is_save:
        cv2.imwrite("./result_example4.jpg", diff)
    
    cv2.imshow("Result", diff)
    cv2.waitKey(0)