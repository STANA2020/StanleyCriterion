# Simulations

This folder will contain Python and OpenFOAM simulation scripts used to test the Stanley Alignment Functional \(\mathcal{A}(t)\) across various fluid scenarios.

## Additional Simulations

These new tests further validate the boundedness and integrability of the alignment functional \(\mathcal{A}(t)\):

- **`channel_obstruction_test.py`**  
  Simulates flow through a turbulent channel with an obstruction.  
  Output: `channel_obstruction_A_t.npy`, `channel_obstruction_A_t.png`

- **`isotropic_turbulence_test.py`**  
  Models decaying 3D isotropic turbulence with randomized vorticity.  
  Output: `isotropic_turbulence_A_t.npy`, `isotropic_turbulence_A_t.png`

- **`vortex_collision_test.py`**  
  Simulates the head-on interaction of two vortex rings.  
  Output: `vortex_collision_A_t.npy`, `vortex_collision_A_t.png`

Each test supports the global integrability of the alignment functional across complex flow structures.

