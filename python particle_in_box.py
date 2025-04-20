import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eigh

# Constants
hbar = 1
m = 1
L = 1.0
N = 1000
x = np.linspace(0, L, N)
dx = x[1] - x[0]

# Discard first and last point to apply boundary condition ψ(0)=ψ(L)=0
x_inner = x[1:-1]
N_inner = len(x_inner)

# Kinetic energy operator (finite difference, second derivative)
coeff = -hbar**2 / (2 * m * dx**2)
main_diag = -2 * np.ones(N_inner)
off_diag = np.ones(N_inner - 1)
H = coeff * (np.diag(main_diag) + np.diag(off_diag, k=1) + np.diag(off_diag, k=-1))

# Solve eigenvalue problem
energies, wavefuncs = eigh(H)

# Normalize wavefunctions
wavefuncs = wavefuncs / np.sqrt(dx)

# Plot first 3 eigenfunctions
plt.figure(figsize=(10, 6))
for n in range(3):
    psi = np.zeros(N)
    psi[1:-1] = wavefuncs[:, n]  # Add boundary zeros
    plt.plot(x, psi, label=f'n={n+1}, E={energies[n]:.4f}')
plt.title("Wavefunctions for Particle in a 1D Box")
plt.xlabel("x")
plt.ylabel("ψ(x)")
plt.legend()
plt.grid(True)
plt.show()