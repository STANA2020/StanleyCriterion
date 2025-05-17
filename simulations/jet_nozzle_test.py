import numpy as np
import matplotlib.pyplot as plt

# Simulated example of A(t) for a Jet Nozzle Flow
def compute_A_t(t):
    return 0.6 + 0.2 * np.exp(-0.5 * t) + 0.1 * np.sin(1.5 * np.pi * t)

def main():
    t_vals = np.linspace(0, 10, 100)
    A_vals = [compute_A_t(t) for t in t_vals]

    # Save raw data
    np.save("jet_nozzle_A_t.npy", A_vals)

    # Plot and save figure
    plt.figure(figsize=(8, 4))
    plt.plot(t_vals, A_vals, color='darkorange', label="A(t): Jet Nozzle Test")
    plt.xlabel("Time")
    plt.ylabel("Alignment Functional A(t)")
    plt.title("Stability of A(t) in a Jet Nozzle Flow")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("jet_nozzle_A_t.png")
    plt.show()

if __name__ == "__main__":
    main()
