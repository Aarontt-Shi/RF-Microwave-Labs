import numpy as np

c = 3e8
mu0 = 4 * np.pi * 1e-7
eta0 = 376.73
sigma = 5.8e7                       # copper

a, b = 1.07e-2, 0.43e-2             # WR-42 inside dimensions
er, tand = 2.55, 0.0015
f, L = 15e9, 0.10

# check which modes get through at 15 GHz
for m, n in [(1, 0), (2, 0), (0, 1), (1, 1), (2, 1)]:
    print("TE%d%d  fc = %.2f GHz" % (m, n,
          c / (2 * np.sqrt(er)) * np.sqrt((m / a) ** 2 + (n / b) ** 2) / 1e9))

k = 2 * np.pi * f * np.sqrt(er) / c
beta = np.sqrt(k ** 2 - (np.pi / a) ** 2)
eta = eta0 / np.sqrt(er)
Rs = np.sqrt(np.pi * f * mu0 / sigma)

ad = k ** 2 * tand / (2 * beta)
ac = Rs * (2 * b * np.pi ** 2 + a ** 3 * k ** 2) / (a ** 3 * b * beta * k * eta)

print("beta =", round(beta, 1), "rad/m")
print("alpha_d =", round(ad, 4), "Np/m  =", round(8.686 * ad, 4), "dB/m")
print("alpha_c =", round(ac, 4), "Np/m  =", round(8.686 * ac, 4), "dB/m")
print("total =", round(8.686 * (ad + ac), 4), "dB/m")
print("loss over 10 cm =", round(8.686 * (ad + ac) * L, 3), "dB")
print("phase delay =", round(beta * L, 3), "rad =", round(np.degrees(beta * L), 1), "deg")
print("lambda_g =", round(2 * np.pi / beta * 100, 3), "cm")
