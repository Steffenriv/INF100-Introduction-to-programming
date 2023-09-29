import math
import matplotlib.pylab as plt
import numpy as np

#x(t) = v0 * t* cos(theta)
#y(t) = v0 * t*sin(theta) - 1/2 * g * t^2
g = 9.81 #m/s^2
V0 = 20 # m/s
N_steps = 101
timerange = np.arange(0, 5.05, 0.05)
timesequence = np.round(timerange, 3).tolist()

def calc_x(time, angle):
    x_pos = []
    for i in range(len(time)):
        x = V0 * time[i] * math.cos(angle)
        x_pos.append(round(x,3))
    return x_pos

def calc_y(time, angle):
    y_pos = []
    for i in range(len(time)):
        y = V0 * time[i] * math.sin(angle) - 0.5 * g * (time[i]**2)
        y_pos.append(round(y,3))
    return y_pos


angles = [30,45,60]
for i in range(len(angles)):
    rad = math.pi / 180 * angles[i]
    xs = calc_x(timesequence, rad)
    ys = calc_y(timesequence, rad)
    new_ys = []
    new_xs = []
    for n in range(len(ys)):
        if ys[n] >= 0:
            new_ys.append(ys[n])
            new_xs.append(xs[n])
    plt.plot(new_xs, new_ys, 'o', label=f"{angles[i]}°")
plt.legend()
plt.savefig("balltrajectory.png")
plt.show()
