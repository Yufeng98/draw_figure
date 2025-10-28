import numpy as np
import matplotlib.pyplot as plt

def gpu_vf_curves():
    f = np.linspace(800, 2400, 200)
    x = (f - f.min()) / (f.max() - f.min())

    v_original = 0.75 + 0.12 * np.power(x, 0.8) + 0.35 * np.power(x, 2.0)
    v_pvta = v_original - (0.03 + 0.02 * x)
    offsets = [-0.025]
    sw_curves = [(v_pvta + off - 0.01 * (0.5 - x)) for off in offsets]

    fig, ax = plt.subplots(figsize=(7, 5), dpi=160)
    ax.plot(f, v_original, label="Original Curve", linewidth=2.5)
    ax.plot(f, v_pvta, label="Hardware-Specific (PVTA) Curve", linewidth=2.5)
    # for i, v_sw in enumerate(sw_curves, start=1):
    #     ax.plot(f, v_sw, linestyle="--", linewidth=1.8, label=f"Software-Specific (Kernel/Data) #{i}")
    ax.plot(f, sw_curves[0], linestyle="--", linewidth=1.8, label=f"Software-Specific (Kernel/Data) Curve")

    # ax.set_title("GPU Voltage-Frequency Variations: Hardware and Software Effects", fontsize=16)
    ax.set_xlabel("Frequency (MHz)", fontsize=20)
    ax.set_ylabel("Voltage (V)", fontsize=20)
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=18)
    ax.tick_params(axis='both', which='major', labelsize=20)
    fig.tight_layout()
    return fig

if __name__ == "__main__":
    fig = gpu_vf_curves()
    fig.savefig("gpu_vf_curves.png", bbox_inches="tight")