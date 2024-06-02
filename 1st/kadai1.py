import cv2
import numpy as np

def fill(image_path, fill_range, fill_color):
    raw_image = cv2.imread(image_path)
    raw_h, raw_w = raw_image.shape[0], raw_image.shape[1]
    center_of_image = (int(raw_w/2), int(raw_h/2))
    modified_image = cv2.circle(raw_image, center_of_image, fill_range, fill_color, thickness=-1)
    return modified_image

if __name__ == '__main__':
    raw_image = "./example1.jpg"
    is_save = False
    modified = fill(raw_image, 100, (0, 0, 0))

    # save result
    if is_save:
        cv2.imwrite("./result_example1.jpg", modified)

    # result visualize
    cv2.imshow("Result", modified)
    cv2.waitKey(0)