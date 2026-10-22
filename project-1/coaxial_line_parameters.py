"""RG-402U semirigid coaxial cable.

Per-unit-length R, L, G, C at 1 GHz, then Z0 and alpha. Also plots the
attenuation from 1 MHz to 100 GHz on a log-log scale.
"""

import numpy as np
import matplotlib.pyplot as plt

mu0, eps0 = 4*np.pi*1e-7, 8.854e-12
sig = 5.813e7          # copper conductivity (S/m)
er, td = 2.08, 4e-4    # Teflon: relative permittivity, loss tangent

a = 0.91e-3/2          # inner radius (m)
b = 3.02e-3/2          # outer inner radius (m)


def pul(f):
    w = 2*np.pi*f
    ds = np.sqrt(2/(w*mu0*sig))
    R = (1/(2*np.pi*a*ds) + 1/(2*np.pi*b*ds)) / sig
    L = (mu0/(2*np.pi)) * np.log(b/a)
    G = w * er*eps0 * td
    C = 2*np.pi*er*eps0 / np.log(b/a)
    return R, L, G, C


# (a) values at 1 GHz
R, L, G, C = pul(1e9)
Z0 = np.sqrt(L/C)
alpha = R/(2*Z0) + G*Z0/2
print(f"R    = {R:.4f} Ohm/m")
print(f"L    = {L*1e9:.2f} nH/m")
print(f"G    = {G:.4e} S/m")
print(f"C    = {C*1e12:.2f} pF/m")
print(f"Z0   = {Z0:.3f} Ohm,  alpha = {8.686*alpha:.4f} dB/m")

# (b) attenuation 1 MHz - 100 GHz
f = np.logspace(6, 11, 600)
Rf, Lf, Gf, Cf = np.array([pul(x) for x in f]).T
Z0f = np.sqrt(Lf/Cf)
a_dB = 8.686*(Rf/(2*Z0f) + Gf*Z0f/2)

plt.figure(figsize=(7, 5))
plt.loglog(f/1e9, a_dB, lw=2)
plt.xlabel('Frequency (GHz)')
plt.ylabel('Attenuation (dB/m)')
plt.grid(True, which='both', ls=':')
plt.tight_layout()
plt.savefig('figures/p24_attenuation.png', dpi=150)
