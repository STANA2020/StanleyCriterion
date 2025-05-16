# The Stanley Criterion for Navier–Stokes Regularity

## Author: Nikee Stanley  
**Date**: May 16, 2025

---

### Overview

This repository presents a novel regularity criterion for the 3D incompressible Navier–Stokes equations, based on the alignment between pressure gradients and vorticity. The key quantity introduced is the **Stanley Alignment Functional**, \(\mathcal{A}(t)\), defined as:

\[
\mathcal{A}(t) = \int_{\mathbb{R}^3} \left| \frac{\nabla p(x,t) \cdot \omega(x,t)}{|\nabla p(x,t)| + \varepsilon} \right| dx
\]

This functional measures geometric coherence in turbulent flow and offers a new route to proving global regularity of solutions.

---

### Contents

- `Stanley_Criterion.pdf`: The full manuscript describing the theory, proof, and results.
- `simulations/`: Python and OpenFOAM scripts for simulating fluid flows and tracking \(\mathcal{A}(t)\).
- `plots/`: Sample visualizations of \(\mathcal{A}(t)\) in key flow scenarios.
- `README.md`: This file.
- `LICENSE`: Open-access license (MIT or Creative Commons recommended).

---

### Key Results

- If \(\mathcal{A}(t)\) is integrable on \([0, T]\), the velocity field remains regular on that interval.
- For smooth, finite-energy initial data, \(\mathcal{A}(t) \in L^1([0,\infty))\), implying global regularity.
- Criterion extended to Leray–Hopf weak solutions.
- Numerical simulations show \(\mathcal{A}(t)\) remains bounded across:
  - Vortex collapse
  - Channel flow
  - Jet nozzles
  - Stratified rotating flows

---

### Citation

Please cite the paper as:

