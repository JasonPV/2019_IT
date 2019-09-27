import matplotlib.pyplot as plt
import numpy as np
import math

#sig = int(input())
#windows_size = int(input())
def add_noise(img, rate=5):
    img[::rate, ::rate, :] = 1
    return

def get_kernel(windows_size, sig = 1):
    kernel = np.zeros((windows_size, windows_size))
    mean = windows_size // 2
    for x in range(windows_size):
        for y in range(windows_size):
            kernel[x][y] = math.exp( (-0.5 * (x - mean) / sig) ** 2.0 + ((y - mean) /sig) ** 2.0) / (2 * math.pi * sig * sig)

    kernel /= kernel.sum()
    return kernel

def filter(img, window_size = 5):
    img2 = np.zeros_like(img)
    kernel = get_kernel(window_size)
    p = window_size//2
    for k in range(img.shape[2]): # foreach color channel
        for i in range(p, img.shape[0]-p): # foreach row
            for j in range(p, img.shape[1]-p): # foreach column
                window = img[i-p:i+p+1, j-p:j+p+1, k]
                img2[i,j,k] = (kernel*window).sum()
    return img2



def main():
    img = plt.imread("img.png")[:, :, :3]
    add_noise(img)
    img2 = filter(img)

    fig, axs = plt.subplots(1,2)
    axs[0].imshow(img)
    axs[1].imshow(img2)
    plt.show()


if __name__ == "__main__":
    main()
