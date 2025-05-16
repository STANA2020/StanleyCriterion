import numpy as np
import matplotlib.pyplot as plt

# Simulated example of A(t) for a 2D vortex
def compute_A_t(t):
    return np.exp(-0.3 * t) + 0.05 * np.sin(2 * np.pi * t)

def main():
    t_vals = np.linspace(0, 10, 100)
    A_vals = [compute_A_t(t) for t in t_vals]

    # Save raw data
    np.save("vortex_A_t.npy", A_vals)

    # Plot and save figure
    plt.figure(figsize=(8, 4))
    plt.plot(t_vals, A_vals, label="A(t): Vortex Test")
    plt.xlabel("Time")
    plt.ylabel("Alignment Functional A(t)")
    plt.title("Decay of A(t) in a 2D Rotating Vortex")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("vortex_A_t.png")
    plt.show()

if __name__ == "__main__":
    main()
