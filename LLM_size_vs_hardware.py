# Create the scatter plot from the provided datasheet
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def make_df(rows, group):
    df = pd.DataFrame(rows, columns=["name", "date_str", "scaling"])
    # Parse month-year like "Jun-18" -> first day of that month/year
    df["date"] = pd.to_datetime(df["date_str"], format="%b-%y")
    df["group"] = group
    return df[["group", "name", "date", "scaling"]]

# Data transcribed from the user's table
model_rows = [
    ("GPT", "Jun-18", 1),
    ("BERT", "Nov-18", 3),
    ("GPT-2", "Nov-19", 13),
    ("ViT", "Oct-20", 5),
    ("Llama", "Feb-22", 569),
    ("BLOOM", "Jul-22", 1540),
    ("Llama2", "Jul-23", 613),
    ("Grok", "Mar-24", 2748),
    ("Mixtral", "Apr-24", 1234),
    ("Grok-2", "Aug-24", 2363),
    ("DeepSeek-V2", "Jun-24", 2066),
    ("Llama3", "Jul-24", 3545),
    ("DeepSeek-V3", "Dec-24", 5873),
    ("Qwen3", "Apr-25", 1969),
    ("Llama4", "Apr-25", 17504),
    ("Kimi-k2", "Jun-25", 8752),
    ("Pangu", "Aug-25", 6284),
    ("Nematron-4", "Sep-25", 2976),
]

hardware_rows = [
    ("P100", "Jun-16", 1),
    ("V100", "Jun-17", 7),
    ("TPUv2", "Dec-17", 2),
    ("TPUv3", "Dec-18", 6),
    ("A100", "Jun-20", 16),
    ("MI100", "Nov-20", 10),
    ("MI250X", "Nov-21", 20),
    ("TPUv4", "Dec-21", 14),
    ("H100", "Sep-22", 52),
    ("MI300X", "Dec-23", 69),
    ("TPUv5p", "Dec-23", 24),
    ("B200", "Dec-24", 135),
    ("TPUv6", "Dec-24", 48),
    ("MI350X", "Jun-25", 122),
    ("TPUv7", "Oct-25", 121),
]

dram_bandwidth_rows = [
    ("P100", "Jun-16", 1),
    ("V100", "Jun-17", 1),
    ("TPUv2", "Dec-17", 1),
    ("TPUv3", "Dec-18", 1),
    ("A100", "Jun-20", 3),
    ("MI100", "Nov-20", 2),
    ("MI250X", "Nov-21", 5),
    ("TPUv4", "Dec-21", 2),
    ("H100", "Sep-22", 5),
    ("MI300X", "Dec-23", 7),
    ("TPUv5p", "Dec-23", 4),
    ("B200", "Dec-24", 11),
    ("TPUv7", "Oct-25", 11),
]

dram_capacity_rows = [
    ("P100", "Jun-16", 1),
    ("V100", "Jun-17", 2),
    ("TPUv2", "Dec-17", 1),
    ("TPUv3", "Dec-18", 2),
    ("A100", "Jun-20", 5),
    ("MI100", "Nov-20", 2),
    ("MI250X", "Nov-21", 8),
    ("TPUv4", "Dec-21", 2),
    ("H100", "Sep-22", 5),
    ("MI300X", "Dec-23", 12),
    ("TPUv5p", "Dec-23", 6),
    ("B200", "Dec-24", 12),
    ("TPUv7", "Oct-25", 12),
]

interconnect_rows = [
    ("NVLink 2", "Dec-17", 1),
    ("NVLink 3", "Dec-20", 2),
    ("NVLink 4", "Dec-22", 3),
    ("NVLink 5", "Dec-24", 6),
]

df = pd.concat(
    [
        make_df(model_rows, "Model Size: 4x per year"),
        make_df(hardware_rows, "Hardware TFLOPS: 73% per year"),
        make_df(interconnect_rows, "Interconnect Bandwidth: 29% per year"),
        make_df(dram_bandwidth_rows, "DRAM Bandwidth: 31% per year"),
        make_df(dram_capacity_rows, "DRAM Capacity: 32% per year"),
    ],
    ignore_index=True,
)

# Create five separate figures
# Define colors for each group
colors = ['red', 'blue', 'orange', 'green', 'red']
group_names = ["Model Size: 4x per year", "Hardware TFLOPS: 73% per year", "Interconnect Bandwidth: 29% per year", "DRAM Bandwidth: 31% per year", "DRAM Capacity: 32% per year"]

# Calculate overall date range for consistent x-axis across all figures
overall_min_date = df["date"].min()
overall_max_date = df["date"].max()

overall_min_date = pd.to_datetime("Dec-15", format="%b-%y")
overall_max_date = pd.to_datetime("Jan-26", format="%b-%y")


def create_plot(groups_to_include, title_suffix, figure_num):
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Plot groups in the desired order to maintain legend order
    for group_name in group_names:
        if group_name in groups_to_include:
            gdf = df[df["group"] == group_name]
            color_idx = group_names.index(group_name)
            color = colors[color_idx]
            ax.scatter(gdf["date"], gdf["scaling"], label=group_name, alpha=1.0, color=color)
            
            # Add name labels near each point
            for _, row in gdf.iterrows():
                ax.annotate(row["name"], 
                           (row["date"], row["scaling"]),
                           xytext=(5, 5), 
                           textcoords="offset points",
                           fontsize=8,
                           alpha=0.8)
    
    # Axes formatting
    ax.set_yscale("log")
    ax.set_ylim(0.5, 300)
    ax.set_xlim(overall_min_date, overall_max_date)  # Set consistent x-axis range
    ax.set_xlabel("Release date", fontsize=16)
    ax.set_ylabel("Scaling (log scale)", fontsize=16)
    # ax.set_title(f"Figure {figure_num}: {title_suffix}", fontsize=16)
    
    # X axis formatting for years
    ax.xaxis.set_major_locator(mdates.YearLocator(base=1))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    fig.autofmt_xdate()
    
    ax.grid(True, which="both", linestyle="--", alpha=0.4)
    legend = ax.legend(loc="upper left", fontsize=16)
    
    # Make legend text bold and set colors to match dots
    for text in legend.get_texts():
        text.set_weight('bold')
        group_name = text.get_text()
        if group_name in group_names:
            color_idx = group_names.index(group_name)
            text.set_color(colors[color_idx])
    
    # Increase tick label font size
    ax.tick_params(axis='both', which='major', labelsize=12)
    
    plt.tight_layout()
    plt.savefig(f"LLM_size_vs_hardware_figure_{figure_num}.png", dpi=300)

# # Figure 1: Only model scaling
# create_plot(["Model Size: 4x per year"], "Model Scaling Only", 1)

# # Figure 2: Model and Hardware TFLOPS scalings
# create_plot(["Model Size: 4x per year", "Hardware TFLOPS: 73% per year"], "Model and Hardware TFLOPS Scaling", 2)

# # Figure 3: Model, Hardware TFLOPS and Interconnect BW Scaling
# create_plot(["Model Size: 4x per year", "Hardware TFLOPS: 73% per year", "Interconnect Bandwidth: 29% per year"], "Model, Hardware TFLOPS and Interconnect BW Scaling", 3)

# # Figure 4: Add DRAM Bandwidth Scaling
# create_plot(["Model Size: 4x per year", "Hardware TFLOPS: 73% per year", "Interconnect Bandwidth: 29% per year", "DRAM Bandwidth: 31% per year"], "All Four Scalings", 4)

# # Figure 5: Model, Hardware TFLOPS, DRAM BW and Capacity (no interconnect)
# create_plot(["Model Size: 4x per year", "Hardware TFLOPS: 73% per year", "DRAM Bandwidth: 31% per year", "DRAM Capacity: 32% per year"], "Model, Hardware TFLOPS, DRAM BW and Capacity", 5)

# # Figure 2: Model, Hardware TFLOPS scalings and DRAM BW
# create_plot(["Model Size: 4x per year", "Hardware TFLOPS: 73% per year", "DRAM Bandwidth: 31% per year"], "Model, Hardware TFLOPS Scaling and DRAM BW", 6)

create_plot(["Hardware TFLOPS: 73% per year"], "Hardware TFLOPS Scaling", 7)

create_plot(["Hardware TFLOPS: 73% per year", "DRAM Bandwidth: 31% per year"], "Model, Hardware TFLOPS Scaling and DRAM BW", 8)

create_plot(["Hardware TFLOPS: 73% per year", "DRAM Bandwidth: 31% per year", "DRAM Capacity: 32% per year"], "Model, Hardware TFLOPS Scaling, DRAM BW and capacity", 9)

