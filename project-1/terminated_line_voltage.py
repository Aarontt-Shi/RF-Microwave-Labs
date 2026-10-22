"""voltage along a terminated transmission line.

Vg = 10 V with Rs = 100 Ohm drives a Z0 = 100 Ohm line of length l = 1.5 lambda
terminated in ZL = 80 - j40 Ohm. Plots |V(z)| for -l <= z <= 0.
"""

import numpy as np
import matplotlib.pyplot as plt

Vg, Rs = 10, 100
Z0, l = 100, 1.5           # line length in wavelengths
ZL = 80 - 40j
beta = 2*np.pi

# load reflection coefficient
Gamma = (ZL - Z0) / (ZL + Z0)

# input impedance seen at the source end
Zin = Z0 * (ZL + 1j*Z0*np.tan(beta*l)) / (Z0 + 1j*ZL*np.tan(beta*l))

# voltage at the source end (voltage divider)
V0 = Vg * Zin / (Rs + Zin)

# At the source end V0 = V+ + V-, and V- = Gamma * V+
Vp = V0 / (1 + Gamma)
Vm = Gamma * Vp

print(f"Z_in   = {Zin:.3f} Ohm")
print(f"V+     = {Vp:.3f} V,  V- = {Vm:.3f} V,  |Gamma| = {abs(Gamma):.3f}")

d = np.linspace(0, l, 600)          # distance from source
V = Vp*np.exp(-1j*beta*d) + Vm*np.exp(1j*beta*d)
z = d - l                           # back to z (load at z = 0)

plt.figure(figsize=(7, 4.5))
plt.plot(z, np.abs(V), lw=2)
plt.xlabel('z (wavelengths; load at 0, source at -l)')
plt.ylabel('|V(z)| (V)')
plt.grid(True, ls=':')
plt.tight_layout()
plt.savefig('figures/p219_voltage.png', dpi=150)
