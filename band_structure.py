import numpy as np
import matplotlib.pyplot as plt
import scipy as sci


'''
Diagonalize matrix and add periodic boundary conditions
'''
def diagonalize_matrix(nsite,j):
    ham = np.zeros((nsite,nsite))

    for n in range(nsite-1):
        ham[n,n+1] = ham[n+1,n] = -j
    
    periodic_boundary_conditions(ham,nsite,j)
    energies, vectors = np.linalg.eigh(ham)
    return energies, vectors


'''
Periodic boundary conditions
'''
def periodic_boundary_conditions(hamiltonian,nsite,j):
    hamiltonian[0,nsite-1] = hamiltonian[nsite-1,0] = -j
    

'''
Calculate momenta and energy
'''
def momenta_energy(energies,vectors,nsite):
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
        
    return momenta, energies





