import numpy as np
import matplotlib.pyplot as plt

# C = np.array([ # C = X + 1j * Y
#     [-1+1j, 1j, 1+1j],
#     [-1, 0, 1],
#     [-1-1j, -1j, 1-1j]
# ])

X = np.linspace(-2.,2.,500)[None,:]
Y = np.linspace(-2.,2.,500)[:,None]

# zoomed in
# X = np.linspace(-0.725,-0.705,5000)[None,:]
# Y = np.linspace(0.335,0.355,5000)[:,None]

print(X.shape, Y.shape)

C = X + 1j * Y
print(C.shape)
print(C)

# startverdien til Z er alltid 0
Z = np.zeros_like(C)

# P teller opp iterasjoner, plottes til slutt
P = np.zeros_like(C, dtype='uint8') # heltall 0..256

print(Z.shape, P.shape)

# iterasjon av Z <- Z*Z + C
for i in range(120):
    # hvilke elementer er fortsett "live"?
    live = np.abs(Z) < 2.
    # oppdater fargen i plot
    P[live] = i 
    # kjør neste iterasjon ()
    Z[live] = Z[live]*Z[live] + C[live] 

plt.imshow(
    P, 
    extent=(X.min(), X.max(), Y.min(), Y.max())
)
plt.colorbar()
#plt.savefig('plot.png')
plt.show()