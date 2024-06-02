import cv2
import numpy as np

def contrast(image_path):
    image_bgr = cv2.imread(image_path) # opencvはBGR形式で読み込む
    image_hsv = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2HSV) # HSV形式に変換
    h, s, v = image_hsv[:,:,0], image_hsv[:,:,1], image_hsv[:,:,2]
    
    # convert contrast
    low_convert = np.where(image_hsv[:, :, 2] < 100, 0, image_hsv[:, :, 2]) #輝度100未満の輝度を0に変更
    high_convert = np.where(low_convert > 150, 255, low_convert) #輝度151以上の輝度を255に変更
    middle_convert = np.where(((high_convert >= 100) & (high_convert <= 150)), 5.1*high_convert-510, high_convert)
    image_hsv[:,:,2] = middle_convert
    return cv2.cvtColor(image_hsv, cv2.COLOR_HSV2BGR)

if __name__ == '__main__':
    raw_image = "./example3.jpg"
    is_save = True
    modified = contrast(raw_image)

    # save result
    if is_save:
        cv2.imwrite("./result_example1.jpg", modified)

    cv2.imshow("Result", modified)
    cv2.waitKey(0)