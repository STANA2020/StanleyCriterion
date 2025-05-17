import numpy as np
import matplotlib.pyplot as plt

def compute_A_t(t):
    np.random.seed(0)
    return 0.5 * np.exp(-0.15 * t) + 0.1 * np.random.rand(len(t))

def main():
    t_vals = np.linspace(0, 10, 100)
    A_vals = compute_A_t(t_vals)

    np.save("isotropic_turbulence_A_t.npy", A_vals)

    plt.figure(figsize=(8, 4))
    plt.plot(t_vals, A_vals, label="A(t): Isotropic Turbulence", color="green")
    plt.xlabel("Time")
    plt.ylabel("Alignment Functional A(t)")
    plt.title("Decaying Isotropic Turbulence")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("isotropic_turbulence_A_t.png")
    plt.show()

if __name__ == "__main__":
    main()
