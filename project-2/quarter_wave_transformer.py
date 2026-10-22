import numpy as np
import matplotlib.pyplot as plt

Z0, RL = 75.0, 40.0
Zt = np.sqrt(Z0 * RL)
print("Zt =", round(Zt, 2), "ohm")

r = np.linspace(0.5, 2.0, 601)          # r = f / f0
bl = np.pi / 2 * r                      # quarter wavelength long when r = 1

Zin = Zt * (RL + 1j * Zt * np.tan(bl)) / (Zt + 1j * RL * np.tan(bl))
G = (Zin - Z0) / (Zin + Z0)
SWR = (1 + abs(G)) / (1 - abs(G))

for rr in (0.5, 0.75, 1.0, 1.25, 1.5, 2.0):
    i = abs(r - rr).argmin()
    print("f/f0 =", rr, "  |Gamma| =", round(abs(G[i]), 4), "  SWR =", round(SWR[i], 4))

plt.figure(figsize=(10, 4))

plt.subplot(121)
plt.plot(r, abs(G), linewidth=2)
plt.xlabel('f / f0', fontsize=12)
plt.ylabel('|Gamma|', fontsize=12)
plt.title('reflection coefficient', fontsize=12)
plt.tick_params(labelsize=12)
plt.grid(True)

plt.subplot(122)
plt.plot(r, SWR, linewidth=2)
plt.xlabel('f / f0', fontsize=12)
plt.ylabel('SWR', fontsize=12)
plt.title('standing wave ratio', fontsize=12)
plt.tick_params(labelsize=12)
plt.grid(True)

plt.tight_layout()
plt.savefig('figures/p224_swr_gamma.png', dpi=200)
