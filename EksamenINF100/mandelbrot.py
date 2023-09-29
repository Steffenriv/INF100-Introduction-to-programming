import numpy as np
import matplotlib.pyplot as plt

def mandel(x, y, size, pixels, filename):   
    xmin, xmax = x, x+size
    ymin, ymax = y, y+size
    num_pixels = pixels

    # initial setup of calculation constant C for each pixel
    X = np.linspace(xmin, xmax, num_pixels)[None,:]
    Y = np.linspace(ymin, ymax, num_pixels)[:,None]
    C = X + 1j * Y
    # start value of Z is always 0
    Z = np.zeros_like(C)
    # P counts iterations, this is what we plot at the end
    P = np.zeros_like(C, dtype='uint8') # unsigned int 0..255

    # iteration of Z <- Z*Z + C
    for i in range(120):
        # print(f"Iteration {i}")
        # which elements are still "live"?
        live = np.abs(Z) < 2.
        # update live pixels with current iteration number
        P[live] = i 
        # iterate
        Z[live] = Z[live]*Z[live] + C[live] 

    plt.imshow(
        P, 
        origin='lower',
        extent=(X.min(), X.max(), Y.min(), Y.max())
    )
    plt.savefig(f"{filename}")

def mandel_zoom(old_x, new_x, old_y, new_y, old_size, new_size, pixels, num_steps):
    x = list(np.linspace(old_x,new_x,num_steps))
    y = list(np.linspace(old_y, new_y, num_steps))
    size = list(np.linspace(old_size, new_size, num_steps))

    for i in range(num_steps):
        mandel(x[i], y[i], size[i], pixels, f"zoom_{i+1}.png")



while True:
    try:
        num_images =  int(input("Antall bilder: "))
        pixels = int(input("Antall piksler: "))
        mandel_zoom(-2, -0.725, -1.5, 0.335, 3, 0.02, pixels, num_images)
        break
    except ValueError:
        continue


