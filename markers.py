import cv2
from matplotlib import pyplot as plt


def main():
    markers = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
    marker = markers.drawMarker(4, 800)

    plt.clf()
    plt.imshow(marker, cmap='gray')
    plt.axis('off')
    plt.show()


if __name__ == "__main__":
    main()
