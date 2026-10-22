"""Reflection coefficient of a line with three terminations.

Reproduces the NRAO Microwave Office exercise numerically: a 50 Ohm line of
fixed physical length terminated in 50 Ohm, a short and an open. Because the
line is electrically short, Zin ~ ZL, so S11 -> 0, -1, +1 respectively.
The main plot is Re(S11) over -2..+2, matching the tutorial's S11_real graph.
"""

import numpy as np
import matplotlib.pyplot as plt

Z0 = 50.0
f0 = 500e6
c0 = 3e8
length = 1e-3                              # 1 mm, electrically short up to 1 GHz

f = np.linspace(0.2*f0, 2.0*f0, 1001)      # 100 MHz - 1 GHz
beta = 2*np.pi*f / c0
tand = np.tan(beta*length)


def S11(ZL):
    Zin = Z0 * (ZL + 1j*Z0*tand) / (Z0 + 1j*ZL*tand)
    return (Zin - Z0) / (Zin + Z0)


S_matched = S11(50.0)
S_short = S11(0.0 + 0j)
S_open = np.exp(-2j*beta*length)           # ZL -> inf  gives  S11 = exp(-2j beta l)

i0 = np.argmin(np.abs(f - f0))
print(f"length = {length*1e3:.1f} mm  ({length/(c0/f0)*100:.2f}% of lambda at 500 MHz)")
for name, s in [('matched', S_matched), ('short', S_short), ('open', S_open)]:
    print(f"{name:8s}: Re(S11) = {s[i0].real:+.4f},  |S11| = {abs(s[i0]):.4f},"
          f"  phase = {np.angle(s[i0], deg=True):+7.2f} deg")

# Re(S11) - the tutorial's S11_real graph
plt.figure(figsize=(7, 5))
plt.plot(f/1e6, S_matched.real, lw=2, label='Matched (50 Ohm)')
plt.plot(f/1e6, S_short.real, lw=2, label='Short')
plt.plot(f/1e6, S_open.real, lw=2, label='Open')
plt.ylim(-2, 2)
plt.xlabel('Frequency (MHz)')
plt.ylabel('Re(S11)')
plt.grid(True, ls=':')
plt.legend()
plt.tight_layout()
plt.savefig('figures/s11_real.png', dpi=150)

# magnitude in dB
plt.figure(figsize=(7, 5))
for name, s, t in [('Matched', S_matched, '-'), ('Short', S_short, '--'), ('Open', S_open, ':')]:
    plt.plot(f/1e6, 20*np.log10(np.maximum(np.abs(s), 1e-12)), t, lw=2, label=name)
plt.ylim(-40, 2)
plt.xlabel('Frequency (MHz)')
plt.ylabel('|S11| (dB)')
plt.grid(True, ls=':')
plt.legend()
plt.tight_layout()
plt.savefig('figures/s11_magnitude.png', dpi=150)

# Smith chart
plt.figure(figsize=(6, 6))
t = np.linspace(0, 2*np.pi, 400)
plt.plot(np.cos(t), np.sin(t), 'k-', lw=1)
for name, s in [('Matched', S_matched), ('Short', S_short), ('Open', S_open)]:
    plt.plot(s.real, s.imag, lw=2, label=name)
plt.gca().set_aspect('equal')
plt.xlim(-1.1, 1.1)
plt.ylim(-1.1, 1.1)
plt.xlabel('Re(S11)')
plt.ylabel('Im(S11)')
plt.grid(True, ls=':')
plt.legend(loc='lower right')
plt.tight_layout()
plt.savefig('figures/s11_smith_chart.png', dpi=150)
