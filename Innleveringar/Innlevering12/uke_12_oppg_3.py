import matplotlib.pyplot as plt
from math import sin

# liste med x-verdier
xs = [n / 10 for n in range(101)]
# 2 ulike lister med y-verdier
ys_1 = [sin(x) for x in xs]
ys_2 = [3 * sin(x) for x in xs]

plt.plot(xs, ys_1, "-.r")
plt.plot(xs, ys_2, "--b")

# pil til første interseksjon                                       
plt.annotate('første interseksjon',                                               #  kilde: matplotlib sine eksempel på piler til punkt, med tekst https://matplotlib.org/stable/gallery/text_labels_and_annotations/annotation_demo.html?highlight=point%20arrows 09.11.21                                                      
            xy=(3.1, 0), xycoords='data',                                     #  estimerer punktet 
            xytext=(0.6, 0.9), textcoords='axes fraction',                           
            arrowprops=dict(facecolor='black', shrink=0.05),                               
            horizontalalignment='right', verticalalignment='bottom')        
# savefig lagrer filene
plt.savefig("uke_12_oppg_3.png")                       
# interaktivt vindu
plt.show()