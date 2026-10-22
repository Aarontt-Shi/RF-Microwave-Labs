import numpy as np

c = 3e8
er, tand, Z0 = 2.2, 0.001, 100.0
d = 0.0762e-2                       # substrate thickness 0.0762 cm

A = (Z0 / 60) * np.sqrt((er + 1) / 2) + (er - 1) / (er + 1) * (0.23 + 0.11 / er)
Wd = 8 * np.exp(A) / (np.exp(2 * A) - 2)
W = Wd * d
ee = (er + 1) / 2 + (er - 1) / 2 / np.sqrt(1 + 12 * d / W)
print("W =", round(W * 1e3, 4), "mm,  eps_e =", round(ee, 4))

# part (a): the 0.51 mm substrate width does not give 100 ohm on 0.762 mm
Wa = 0.4571e-3
eea = (er + 1) / 2 + (er - 1) / 2 / np.sqrt(1 + 12 * d / Wa)
Z0a = 60 / np.sqrt(eea) * np.log(8 * d / Wa + Wa / (4 * d))
print("(a) W = 0.4571 mm -> Z0 =", round(Z0a, 2), "ohm, |S11| =",
      round(abs((Z0a - Z0) / (Z0a + Z0)), 4))
print("(b) retune to W =", round(W * 1e3, 4), "mm for 100 ohm")

f = 2.5e9
beta = 2 * np.pi * f * np.sqrt(ee) / c
print("beta =", round(beta, 3), "rad/m,  lambda_g =", round(2 * np.pi / beta * 1e3, 3), "mm")

# open ended line: Zin = -j Z0 cot(beta*l), so tan(beta*l) = -Z0 / X
Xc = -1 / (2 * np.pi * f * 5.0e-12)
bl = np.arctan(-Z0 / Xc)
print("(c) 5 pF -> X =", round(Xc, 3), "ohm, l =", round(bl / beta * 1e3, 3), "mm, S11 phase =",
      round(np.degrees(np.pi + 2 * np.arctan(Xc / Z0)), 1), "deg")

Xl = 2 * np.pi * f * 5.0e-9
bl = np.arctan(-Z0 / Xl) + np.pi
print("(d) 5 nH -> X =", round(Xl, 3), "ohm, l =", round(bl / beta * 1e3, 3), "mm, S11 phase =",
      round(np.degrees(np.pi - 2 * np.arctan(Xl / Z0)), 1), "deg")
