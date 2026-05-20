import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mp

img = mp.imread("img.jpg")

g = np.mean(img[:, :, :3], axis=2)

b1 = np.clip(g + 40, 0, 255)
b2 = np.clip(g - 40, 0, 255)

h = np.fliplr(g)
v = np.flipud(g)

c = g[100:300, 100:300]

fig, ax = plt.subplots(2, 3, figsize=(12, 8))

ax[0,0].imshow(g, cmap='gray')
ax[0,0].set_title("Gray")

ax[0,1].imshow(b1, cmap='gray')
ax[0,1].set_title("Bright")

ax[0,2].imshow(b2, cmap='gray')
ax[0,2].set_title("Dark")

ax[1,0].imshow(h, cmap='gray')
ax[1,0].set_title("Horizontal")

ax[1,1].imshow(v, cmap='gray')
ax[1,1].set_title("Vertical")

ax[1,2].imshow(c, cmap='gray')
ax[1,2].set_title("Crop")

for i in ax.flat:
    i.axis("off")

plt.show()

k = np.array([[1,1,1],
              [1,1,1],
              [1,1,1]]) / 9

bl = np.zeros_like(g)

for i in range(1, g.shape[0]-1):
    for j in range(1, g.shape[1]-1):
        bl[i,j] = np.sum(g[i-1:i+2, j-1:j+2] * k)

plt.imshow(bl, cmap='gray')
plt.title("Blur")
plt.axis("off")
plt.show()