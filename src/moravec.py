import cv2
import numpy as np
import sys


def draw_corners(image, corners_map):
    for corner in corners_map:
        cv2.circle(image, (corner[1], corner[0]), 1, (0, 255, 0), -1)


def moravec(image, threshold=50):
    corners = []
    xy_shifts = [(1, 0), (1, 1), (0, 1), (-1, 1)]
    width, height = image.shape[:2]
    for y in range(1, height - 1):
        for x in range(1, width - 1):
            # Look for local maxima in min(E) above threshold:

            E = 10000000
            for shift in xy_shifts:
                diff = image[x + shift[0], y + shift[1]]

                diff = ((diff - image[x, y]) ** 2)


                if diff < E:
                    E = diff

            if E > threshold:
                corners.append((x, y))

    return corners


if __name__ == "__main__":

    """
    Usage: python moravec.py [-i image] [-t threshold] [-o output path]
    -i /home/nam/Dropbox/hk181/image_processing/asm/image/geo_shapes.png -o /home/nam/Dropbox/hk181/image_processing/asm/output/moravec_geo_shapes.png
    """


    image_path = "/home/nam/Dropbox/hk181/image_processing/asm/image/corner.jpg"

    threshold = 100

    if "-i" in sys.argv:
        image_path = str(sys.argv[sys.argv.index("-i") + 1])

    if "-t" in sys.argv:
        threshold = int(sys.argv[sys.argv.index("-t") + 1])

    output_img = "/home/nam/Dropbox/hk181/image_processing/asm/output/moravec_corner.jpg"

    if "-o" in sys.argv:
        output_img = str(sys.argv[sys.argv.index("-o") + 1])

    image_RGB = cv2.imread(image_path)
    image = cv2.imread(image_path, 0)

    corners = moravec(image, threshold)

    print("total corner point: ", len(corners))

    draw_corners(image_RGB, corners)

    cv2.imshow('image', image_RGB)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imwrite(output_img, image_RGB)
