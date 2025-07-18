
#!/usr/bin/env python3
"""Rod Impact Simulator
Author: OpenAI Assistant
Date: 2025‑07‑15

Quick‑look tool for estimating ground‑impact effects of a
hyper‑velocity cylindrical projectile such as a tungsten 'Rod from God'.

Physics approach:
  • Kinetic energy from classical mechanics.
  • TNT equivalent conversion (1 t TNT = 4.184 GJ).
  • Crater diameter from empirical nuclear‑test scaling:
        D ≈ 100 m × (Yield_kT)^{1/3}
    (Glasstone & Dolan 1977, valid for surface burst in rock/soil).
  • Blast radii for 1 psi and 5 psi overpressure from the same source.
  • Seismic magnitude via Gutenberg‑Richter energy relation.

**Order‑of‑magnitude tool.**  For engineering work use hydrocodes.

Usage example:
    python rod_impact_sim.py --length 6 --diameter 0.3 --density 19300 \
                             --velocity 11000 --angle 90
"""

import math
import argparse

G = 9.81                 # gravity, m s⁻²
TNT_J_PER_TON = 4.184e9  # conversion factor

def volume_cylinder(L, d):
    r = d / 2
    return math.pi * r * r * L

def mass_cylinder(L, d, rho):
    return volume_cylinder(L, d) * rho

def kinetic_energy(m, v):
    return 0.5 * m * v**2

def tnt_equiv_j_to_ton(E):
    return E / TNT_J_PER_TON

def crater_diameter_m(energy_tons_TNT):
    # Convert to kilotons
    Y_kT = energy_tons_TNT / 1000
    return 100 * (Y_kT ** (1/3))

def blast_radius_km(energy_tons_TNT, overpressure_psi):
    # Cube‑root scaling law (Glasstone & Dolan, 1977)
    coeff = {1:4.5, 5:1.6, 10:1.0}
    if overpressure_psi not in coeff:
        raise ValueError("Choose overpressure 1, 5, or 10 psi")
    return coeff[overpressure_psi] * ((energy_tons_TNT/1000) ** (1/3))

def seismic_magnitude(E):
    # Mw from energy (Kanamori, 1977)
    return (2/3) * math.log10(E) - 3.2

def run(args):
    m = mass_cylinder(args.length, args.diameter, args.density)
    E = kinetic_energy(m, args.velocity)
    E_ton = tnt_equiv_j_to_ton(E)

    crater = crater_diameter_m(E_ton)
    blast5 = blast_radius_km(E_ton, 5)
    blast1 = blast_radius_km(E_ton, 1)
    Mw = seismic_magnitude(E)

    print(f"""=== Hypervelocity Rod Impact ===
Rod parameters
  • Length            : {args.length:.3f} m
  • Diameter          : {args.diameter:.3f} m
  • Density           : {args.density:,} kg/m³
  • Mass              : {m:,.0f} kg

Impact conditions
  • Velocity          : {args.velocity:,.0f} m/s
  • Impact angle      : {args.angle}°
  • Kinetic energy    : {E:,.2e} J
  • TNT equivalent    : {E_ton:,.1f} tons

Estimated effects
  • Crater dia.       : {crater:.1f} m
  • Blast radius 5 psi: {blast5:.2f} km
  • Blast radius 1 psi: {blast1:.2f} km
  • Seismic magnitude : Mw {Mw:.2f}
==========================================""")

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Hypervelocity Rod Impact Simulator (order‑of‑magnitude)")
    p.add_argument("--length", type=float, default=6.0, help="Rod length (m)")
    p.add_argument("--diameter", type=float, default=0.3, help="Rod diameter (m)")
    p.add_argument("--density", type=float, default=19300, help="Rod density (kg/m³)")
    p.add_argument("--velocity", type=float, default=11000, help="Impact velocity (m/s)")
    p.add_argument("--angle", type=float, default=90, help="Impact angle in degrees (from horizontal)")
    args = p.parse_args()
    run(args)
