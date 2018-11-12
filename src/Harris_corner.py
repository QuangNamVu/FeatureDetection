import cv2
import numpy as np

threshold = 0.01
filename = "/home/nam/Dropbox/hk181/image_processing/asm/image/geo_shapes.png"
output_img = "/home/nam/Dropbox/hk181/image_processing/asm/output/Harris_geo_shapes.png"

img = cv2.imread(filename)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

# cv2.CornerHarris(image, harris_dst, blockSize, aperture_size=3, k=0.04)
dst = cv2.cornerHarris(gray, 2, 3, 0.04)

# result is dilated for marking the corners, not important
dst = cv2.dilate(dst, None)

corner_map = dst[dst > threshold * dst.max()]

print("Total %d points" %np.count_nonzero(corner_map))
img[dst > threshold * dst.max()] = [0, 255, 0]

cv2.imshow('dst', img)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()

cv2.imwrite(output_img, img)
