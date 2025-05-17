import numpy as np
import matplotlib.pyplot as plt

def compute_A_t(t):
    return 0.8 * np.exp(-0.2 * t) + 0.05 * np.sin(4 * np.pi * t)

def main():
    t_vals = np.linspace(0, 10, 100)
    A_vals = [compute_A_t(t) for t in t_vals]

    np.save("channel_obstruction_A_t.npy", A_vals)

    plt.figure(figsize=(8, 4))
    plt.plot(t_vals, A_vals, label="A(t): Channel w/ Obstruction", color="blue")
    plt.xlabel("Time")
    plt.ylabel("Alignment Functional A(t)")
    plt.title("Channel Flow with Obstruction")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("channel_obstruction_A_t.png")
    plt.show()

if __name__ == "__main__":
    main()
