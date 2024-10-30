import numpy as np
import imageio as img
import matplotlib.pyplot as plt

path = "C:/Users\Aspire_Black\Pictures\sesi6.png"
image = img.imread(path)

height, width = image.shape[:2]
mirrored = np.zeros_like(image)

for y in range(height):
    for x in range(width):
        mirrored[height - 1 - y, width - 1 - x] = image[y, x]

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.subplot(1, 2, 2)
plt.imshow(mirrored)
plt.show()