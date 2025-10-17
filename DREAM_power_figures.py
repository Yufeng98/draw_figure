# Plot three separate dotted-line charts using matplotlib (no explicit colors).
import matplotlib.pyplot as plt

# Data from the table
labels = ["Vector\nMAC", "1×16\nSA", "2×16\nSA", "4×16\nSA", "8×16\nSA", "16×16\nSA"]
throughput = [1, 1, 1.9, 3.5, 5.7, 8.1]
pu_power = [1, 1.1, 1.4, 2.1, 3.1, 7.9]
device_power = [1, 1.00, 1.2, 1.4, 1.8, 3.3]

# 1) Throughput only
plt.figure()
plt.plot(labels, throughput, linestyle="-", marker="o", markersize=8, label="Throughput")
plt.xlabel("PU design", fontdict={'fontsize': 18})
plt.ylabel("Scaling Factor", fontdict={'fontsize': 18})
plt.legend(fontsize=16)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.tight_layout()
plt.savefig("DREAM_power_figures_1.png")

# 2) Throughput + PU Power
plt.figure()
plt.plot(labels, throughput, linestyle="-", marker="o", markersize=8, label="Throughput")
plt.plot(labels, pu_power, linestyle="-", marker="o", markersize=8, label="PU Power")
plt.xlabel("PU design", fontdict={'fontsize': 18})
plt.ylabel("Scaling Factor", fontdict={'fontsize': 18})
plt.legend(fontsize=16)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.tight_layout()
plt.savefig("DREAM_power_figures_2.png")

# 3) All three lines
plt.figure()
plt.plot(labels, throughput, linestyle="-", marker="o", markersize=8, label="Throughput")
plt.plot(labels, pu_power, linestyle="-", marker="o", markersize=8, label="PU Power")
plt.plot(labels, device_power, linestyle="-", marker="o", markersize=8, label="Device Power")
plt.xlabel("PU design", fontdict={'fontsize': 18})
plt.ylabel("Scaling Factor", fontdict={'fontsize': 18})
plt.legend(fontsize=16)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.tight_layout()
plt.savefig("DREAM_power_figures_3.png")
