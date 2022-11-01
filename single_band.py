'''
Author: Tim Berkelbachj
Purpose: To calculate and plot a single band structure 
using the tight binding model
'''

'''
Tight Binding Model Equation
E = e_0 - 2Jcos(2ka) dispersion relation for a 1d tight binding model

e_0 - energy electron has to remain in atomic orbital

J - hopping strength

k - wave vector

a - lattice 
'''

'''
run: eval "$(pyenv virtualenv-init -)" to start virtual environment in terminal
''' 

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

j = 1.0
nsite = 100

ham = np.zeros((nsite,nsite))

# Diagonalize matrix
for n in range(nsite-1):
    ham[n,n+1] = ham[n+1,n] = -j

# Periodic boundary conditions
ham[0,nsite-1] = ham[nsite-1,0] = -j

# If nsite is small, print ham to see what it looks like
# print(ham)
energies, vectors = np.linalg.eigh(ham)

# these energies include both k and -k, so we have to do
# some work to separate and sort them
momenta = list()
for j,e in enumerate(energies):
    if j%2 == 0:
        momenta.append(j*np.pi/nsite)
    else:
        momenta.append(-j*np.pi/nsite)
momenta = np.array(momenta)
idxs = np.argsort(momenta)

momenta = momenta[idxs]
energies = energies[idxs]


# for k,e in zip(momenta, energies): 
#     print(k, e)

plt.plot(momenta, energies)
plt.xlabel("momenta")
plt.ylabel("energies")
plt.show()
plt.savefig("single_band.png")