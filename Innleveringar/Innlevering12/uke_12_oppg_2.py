import matplotlib.pyplot as plt
from math import sin

# liste med x-verdier
xs = [n / 10 for n in range(101)]
# 2 ulike lister med y-verdier
ys_1 = [sin(x) for x in xs]
ys_2 = [3 * sin(x) for x in xs]

plt.plot(xs, ys_1, "-.r")
plt.plot(xs, ys_2, "--b")

# minor ticks
plt.minorticks_on() # kilde: fant via matplotlib sin nettside matplotlib.org https://matplotlib.org/stable/gallery/specialty_plots/mri_with_eeg.html#sphx-glr-gallery-specialty-plots-mri-with-eeg-py 09.11.21

# savefig lagrer filene
plt.savefig("uke_12_oppg_2.png") 

# interaktivt vindu
plt.show()