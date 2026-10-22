# RF & Microwave Engineering

![Domain](https://img.shields.io/badge/domain-RF%20%2F%20microwave-red)
![Simulator](https://img.shields.io/badge/AWR_Design_Env-25.1-blueviolet)
![Language](https://img.shields.io/badge/language-Python-blue)
![Stack](https://img.shields.io/badge/stack-NumPy%20%2B%20Matplotlib-orange)

Transmission-line and microwave design work: theory derived analytically, then checked against
simulation in AWR Design Environment. Every number in the reports is reproduced by a script in the
same directory, so the arithmetic can be verified rather than taken on trust, and the AWR project
files are committed alongside the reports so each schematic can be reopened and re-run.

Each project lives in its own directory with its own README, which is the complete write-up for
that piece of work.

---

## Projects

| Directory | Topics | Contents |
|---|---|---|
| [`project-1/`](project-1/) | Plane waves, coaxial per-unit-length parameters, terminated-line standing waves, S-parameters | Four analyses plus an AWR reflection-coefficient study; Python for every calculation, plots for every result, AWR project in `awr/s11_reflection/` |
| [`project-2/`](project-2/) | Quarter-wave transformers, rectangular-waveguide loss, stripline / microstrip synthesis, matching stubs | Four analyses plus an AWR microstrip matching study (four sub-circuits in `awr/`) |

More will be added as the work progresses.

---

## What this demonstrates

| Skill | Where it shows up |
|---|---|
| **Transmission-line theory** | Per-unit-length R/L/G/C from skin depth, input impedance, reflection coefficient, VSWR |
| **Impedance matching** | λ/4 transformer synthesis (√(Z₀R_L)), single-stub capacitive / inductive equivalents, frequency response of a narrowband match |
| **S-parameters** | `S11` for matched / open / short terminations, read on both a rectangular plot and a Smith chart |
| **Waveguide & planar media** | TE-mode cutoff counting in a dielectric-filled WR-42 guide, α_d vs α_c decomposition, stripline and microstrip width synthesis |
| **EM simulation** | Schematics built in AWR Design Environment 25.1 from ideal `TLINP` / `TLOCP` / `TLSCP` models and the `MLIN` microstrip model; projects committed as `.emp` / `.vin` / `.dsf` |
| **Reproducible computation** | One Python script per analysis; results printed to stdout and plotted to `figures/` |
| **Physical reasoning** | Discrepancies against datasheet values are explained (conductor surface roughness vs. the smooth-conductor assumption; loss tangent four times the reference Teflon value) |
| **Working shown** | Handwritten derivations kept alongside the typed results so the reasoning is visible |

## Environment

| Component | Version |
|---|---|
| AWR Design Environment | 25.1 |
| Python | 3.13 |
| NumPy | 2.x |
| Matplotlib | 3.x |

## Repository layout

```
.
├── project-1/
│   ├── README.md                      # full write-up with every result tabulated
│   ├── plane_wave.py                  # plane wave quantities in polystyrene
│   ├── coaxial_line_parameters.py     # R, L, G, C, Z0, attenuation sweep
│   ├── terminated_line_voltage.py     # |V(z)| along a terminated line
│   ├── s11_reflection.py              # S11 for matched / short / open
│   ├── figures/                       # plots, AWR screenshots, handwritten derivation
│   ├── awr/s11_reflection/            # AWR 25.1 project: .emp, .vin, netlist, data set
│   └── requirements.txt
├── project-2/
│   ├── README.md                      # full write-up with every result tabulated
│   ├── quarter_wave_transformer.py    # |Gamma| and SWR vs f/f0 for a lambda/4 transformer
│   ├── waveguide_loss.py              # WR-42 alpha_d, alpha_c, phase delay
│   ├── stripline_microstrip_synthesis.py # stripline and microstrip synthesis
│   ├── microstrip_matching.py         # matching widths, eps_e, stub lengths
│   ├── figures/                       # plots
│   ├── awr/                           # AWR 25.1 projects lab2a-lab2d (+ lab2d data set)
│   └── requirements.txt
└── .gitattributes / .gitignore
```

To reproduce any project's numbers:

```bash
pip install -r project-1/requirements.txt
python project-1/coaxial_line_parameters.py

pip install -r project-2/requirements.txt
python project-2/quarter_wave_transformer.py
```

Run scripts from their own directory so the relative figure paths resolve.

## Author

**Aaron (Tianle) Shi** — electrical engineering (RF / hardware focus). Open an issue if you would
like to discuss any of the results here.
