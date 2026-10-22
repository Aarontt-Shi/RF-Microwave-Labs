import numpy as np

c = 3e8
mu0 = 4 * np.pi * 1e-7
sigma = 5.8e7
er, tand, Z0 = 2.20, 0.001, 100.0
f, t = 5e9, 0.035e-3
Rs = np.sqrt(np.pi * f * mu0 / sigma)
lam0 = c / f

# (a) stripline, ground plane spacing b = 1.02 mm
b = 1.02e-3
x = 30 * np.pi / (np.sqrt(er) * Z0) - 0.441
Wb = 0.85 - np.sqrt(0.6 - x)        # sqrt(er)*Z0 = 148 > 120, so this branch
W = Wb * b
We = b * (Wb - (0.35 - Wb) ** 2)    # W/b < 0.35 so the width correction applies

k = 2 * np.pi * f * np.sqrt(er) / c
B = 1 + b / (0.5 * W + 0.7 * t) * (0.5 + 0.414 * t / W + np.log(4 * np.pi * W / t) / (2 * np.pi))
ad = k * tand / 2
ac = 0.16 * Rs * B / (Z0 * b)

print("stripline  W =", round(W * 1e3, 4), "mm   W/b =", round(Wb, 4), "  We/b =", round(We / b, 4))
print("  alpha_d =", round(ad, 4), "Np/m  =", round(8.686 * ad, 4), "dB/m")
print("  alpha_c =", round(ac, 4), "Np/m  =", round(8.686 * ac, 4), "dB/m")
print("  lambda_g =", round(lam0 / np.sqrt(er) * 1e3, 3), "mm")

# (b) microstrip, substrate thickness d = 0.51 mm
d = 0.51e-3
A = (Z0 / 60) * np.sqrt((er + 1) / 2) + (er - 1) / (er + 1) * (0.23 + 0.11 / er)
Wd = 8 * np.exp(A) / (np.exp(2 * A) - 2)
Wm = Wd * d
ee = (er + 1) / 2 + (er - 1) / 2 / np.sqrt(1 + 12 * d / Wm)
k0 = 2 * np.pi * f / c
adm = k0 * er * (ee - 1) * tand / (2 * np.sqrt(ee) * (er - 1))
acm = Rs / (Z0 * Wm)

print("microstrip  W =", round(Wm * 1e3, 4), "mm   W/d =", round(Wd, 4), "  eps_e =", round(ee, 4))
print("  alpha_d =", round(adm, 4), "Np/m  =", round(8.686 * adm, 4), "dB/m")
print("  alpha_c =", round(acm, 4), "Np/m  =", round(8.686 * acm, 4), "dB/m")
print("  lambda_g =", round(lam0 / np.sqrt(ee) * 1e3, 3), "mm")
