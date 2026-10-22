"""uniform plane wave in polystyrene.

E = E0 cos(wt - kx) a_y travelling along +x in a non-magnetic dielectric
(eps_r = 2.54). Computes the H field amplitude, phase velocity, wavelength
and the phase shift between x1 = 0.1 m and x2 = 0.15 m.
"""

import numpy as np

eps_r = 2.54        # polystyrene
f = 2.4e9           # Hz
E0 = 5.0            # V/m
c0 = 3e8            # m/s
eta0 = 376.73       # Ohm, free-space wave impedance

eta = eta0 / np.sqrt(eps_r)
H0 = E0 / eta
vp = c0 / np.sqrt(eps_r)
lam = vp / f
k = 2 * np.pi / lam
dphi = k * (0.15 - 0.10)

print(f"eta     = {eta:.2f} Ohm")
print(f"H0      = {H0*1e3:.2f} mA/m   (E x H along +x  ->  H along +z)")
print(f"v_p     = {vp:.4e} m/s")
print(f"lambda  = {lam:.4f} m")
print(f"k       = {k:.3f} rad/m")
print(f"dphi    = {dphi:.4f} rad = {np.degrees(dphi):.1f} deg")
