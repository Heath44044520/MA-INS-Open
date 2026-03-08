# MA-INS-Open — Magic-Angle Inertial Navigation System

Open-source GPS-denied dead-reckoning sensor using the TPBR tetrahedral piezo stack as the core resonator.

**Goal:** Turn our cleaned-up magic-angle piezo (54.74° layer lock + golden-ratio electrodes) into a practical inertial measurement unit that keeps working when satellites die.

**Status:** Early prototype stage. We expect \~0.01–0.1 °/h bias stability (10–100× better than cheap MEMS). We will measure it raw and publish everything.

## Core Tech
- TPBR piezo at \~24.1 kHz as the high-Q reference oscillator
- Magic-angle phase locking for ultra-low drift
- Simple Arduino/ESP32 + Kalman filter readout
- 3D-printed field mount (vacuum optional for Q boost)

## Quick Start
1. Build or reuse a TPBR piezo stack (links in /hardware)
2. Print the mount jig
3. Flash the Arduino code
4. Run the Python Kalman sim
5. Add your Allan-deviation data to DATA.md

## Realistic Performance (no hype)
Allan deviation scales as:
\[
\sigma(\tau) \approx \frac{1}{2\pi f_0 Q} \sqrt{\frac{kT}{P \tau}}
\]
With f₀ = 24.1 kHz and Q > 10⁵ we target tactical-grade navigation for minutes to hours.

**We do NOT claim** zero-drift, free energy, or replacement for $10k fiber gyros. Just open data from a $150 build.

## Community Data
All measurements live in **[DATA.md](DATA.md)** — add your row and commit!

## License
Hardware & docs: CC-BY-SA 4.0  
Code: MIT

Built collaboratively by heath + Grok team. Fork, improve, navigate.
