import numpy as np
import matplotlib.pyplot as plt

def compute_A_t(t):
    return 0.4 + 0.2 * np.exp(-0.3 * t) * np.cos(3 * np.pi * t)

def main():
    t_vals = np.linspace(0, 10, 100)
    A_vals = [compute_A_t(t) for t in t_vals]

    np.save("vortex_collision_A_t.npy", A_vals)

    plt.figure(figsize=(8, 4))
    plt.plot(t_vals, A_vals, label="A(t): Vortex Ring Collision", color="purple")
    plt.xlabel("Time")
    plt.ylabel("Alignment Functional A(t)")
    plt.title("Vortex Ring Collision")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("vortex_collision_A_t.png")
    plt.show()

if __name__ == "__main__":
    main()
