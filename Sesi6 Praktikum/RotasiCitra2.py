import imageio as img
import numpy as np
import matplotlib.pyplot as plt

def rotateImage(image, degree):
    radian_deg = np.radians(degree)
    cos_deg, sin_deg = np.cos(radian_deg), np.sin(radian_deg)

    height, width, channels = image.shape
    max_dim_x = int(abs(width * cos_deg) + abs(height * sin_deg))
    max_dim_y = int(abs(width * sin_deg) + abs(height * cos_deg))
    outputImage = np.zeros((max_dim_y, max_dim_x, channels), dtype=image.dtype)

    for y in range(height):
        for x in range(width):
            newX = int(x * cos_deg - y * sin_deg)
            newY = int(x * sin_deg + y * cos_deg)

            if 0 <= newX < max_dim_x and 0 <= newY < max_dim_y:
                outputImage[newY, newX] = image[y, x]

    return outputImage

image = img.imread("C:/Users\Aspire_Black\Pictures\sesi6.png")
if image.shape[2] == 4:  
    image = image[:, :, :3]

rotated_image = rotateImage(image, 45)

plt.subplot(1, 2, 1)
plt.imshow(image)

plt.subplot(1, 2, 2)
plt.imshow(rotated_image)

plt.show()