'''
Main Program
'''

import band_structure as band
import matplotlib.pyplot as plt


j = [1.0,2.0,3.0]
nsite = 100

for i in j:
    energy, vector = band.diagonalize_matrix(nsite, i)
    momenta, energies = band.momenta_energy(energy, vector, nsite)
    
    plt.plot(momenta, energies)

plt.xlabel("momenta")
plt.ylabel("energies")
plt.show()
plt.savefig("two_band_structures.png")