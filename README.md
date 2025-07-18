
# Rod Impact Simulator 🛰️💥

A fast and lightweight simulation tool for modeling the effects of a hypervelocity kinetic impact from a cylindrical projectile (aka a "Rod from God").  
Perfect for conceptual studies, sci-fi research, early-stage orbital weapons modeling, or shock physics hobbyists.

---

## 📌 Features

This tool computes:

- ✅ Kinetic energy from customizable rod parameters
- ✅ TNT-equivalent yield conversion
- ✅ Crater diameter using nuclear impact scaling laws
- ✅ Blast radii for 1 psi and 5 psi overpressure zones
- ✅ Seismic magnitude from kinetic impact energy
- ✅ Optional: Export results to JSON for further integration

---

## ⚙️ Requirements

- Python 3.x  
- No external dependencies — uses only standard Python libraries: `math`, `argparse`, and optionally `json`

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/Devsliger/rod-impact-sim.git
cd rod-impact-sim
```

### 2. Run the Script with Default Parameters

```bash
python rod_impact_sim.py
```

This runs the simulation using default values:

- Length: `6.0 m`
- Diameter: `0.3 m`
- Density: `19300 kg/m³` (Tungsten)
- Velocity: `11000 m/s`
- Angle: `90°` (vertical impact)

---

## 🛠️ Custom Input (CMD or Git Bash)

Use CLI flags to pass custom values:

```bash
python rod_impact_sim.py --length 8 --diameter 0.4 --density 16000 --velocity 12500 --angle 85
```

### ✅ Supported Flags

| Flag        | Description                 | Default  |
|-------------|-----------------------------|----------|
| `--length`  | Rod length in meters        | `6.0`    |
| `--diameter`| Rod diameter in meters      | `0.3`    |
| `--density` | Rod density in kg/m³        | `19300`  |
| `--velocity`| Impact velocity in m/s      | `11000`  |
| `--angle`   | Impact angle in degrees     | `90`     |

---

## ⚡ Example Output

```yaml
=== Hypervelocity Rod Impact ===

Rod parameters:
  • Length            : 6.000 m
  • Diameter          : 0.300 m
  • Density           : 19,300 kg/m³
  • Mass              : 8,177 kg

Impact conditions:
  • Velocity          : 11,000 m/s
  • Impact angle      : 90°
  • Kinetic energy    : 4.95e+11 J
  • TNT equivalent    : 118.3 tons

Estimated effects:
  • Crater diameter   : 59.1 m
  • Blast radius 5 psi: 0.84 km
  • Blast radius 1 psi: 2.36 km
  • Seismic magnitude : Mw 3.63

==========================================
```

---

## 🔄 Optional Features (Coming Soon)

- Export to `.json` for data reuse or visualization
- Live matplotlib plot of crater + blast radii
- Map overlay using `folium` or `geopandas` (for real cities like Rabat)
- KML/GeoJSON export for Google Earth or QGIS use

---

## 🧠 Disclaimer

This simulator provides **first-order approximations only**. It's built for educational, research, and speculative modeling. Not intended for actual engineering design, real-world policy simulation, or military application.

---

## 🤝 Contributions

Pull requests and forks are welcome. If you’ve got a crazy idea — nuclear rod in Minecraft, impact on Mars, or AI-generated blast maps — submit an issue or open a PR.

---

## 📜 License

MIT License — free to use, modify, redistribute. Attribution appreciated.
