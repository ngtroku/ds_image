import numpy as np
import cv2
import matplotlib.pyplot as plt

def show_hist(image_path):
    raw_image = cv2.imread(image_path)
    b, g, r = raw_image[:, :, 0], raw_image[:, :, 1], raw_image[:, :, 2]
    hist_b, hist_g, hist_r = cv2.calcHist([b],[0],None,[256],[0,256]), cv2.calcHist([g],[0],None,[256],[0,256]), cv2.calcHist([r],[0],None,[256],[0,256])
    return hist_b, hist_g, hist_r

if __name__ == '__main__':
    raw_image = "./example2.jpg"
    hist_b, hist_g, hist_r = show_hist(raw_image)

    # visualize
    fig = plt.figure(figsize=(12, 6))
    plt.subplots_adjust(wspace=0.4)
    ax1 = fig.add_subplot(1, 3, 1)
    ax2 = fig.add_subplot(1, 3, 2)
    ax3 = fig.add_subplot(1, 3, 3)
    ax1.plot(hist_b, color="blue", label="B")
    ax2.plot(hist_g, color="green", label="G")
    ax3.plot(hist_r, color="red", label="R")
    ax1.set_xticks([32 * i for i in range(9)])
    ax2.set_xticks([32 * i for i in range(9)])
    ax3.set_xticks([32 * i for i in range(9)])
    ax1.legend()
    ax2.legend()
    ax3.legend()
    plt.show()
