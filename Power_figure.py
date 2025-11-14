"""Plot global data center Energy consumption projections."""

from __future__ import annotations

import matplotlib.pyplot as plt

plt.rcParams.update({
	"font.size": 16,
	"axes.labelsize": 18,
	"xtick.labelsize": 16,
	"ytick.labelsize": 16,
})


YEARS = [
	2015,
	2016,
	2017,
	2018,
	2019,
	2020,
	2021,
	2022,
	2023,
	2024,
	2025,
	2026,
	2027,
	2028,
	2029,
	2030,
]

CONSUMPTION_TWH = [
	200,
	200,
	200,
	205,
	205,
	225,
	270,
	290,
	360,
	415,
	477,
	549,
	631,
	726,
	835,
	960,
]

COUNTRY_CONSUMPTION_TWH = {
	"China": 8900,
	"United States": 4100,
	"India": 1500,
	"Russia": 1000,
	"Japan": 913.2,
	"Brazil": 610.4,
	"South Korea": 564.2,
	"Canada": 549.8,
	"Germany": 475.9,
	"France": 412.6,
}


IDX_2019 = YEARS.index(2019)
IDX_2024 = YEARS.index(2024)

YEARS_PRE_2020 = YEARS[: IDX_2019 + 1]
DATA_PRE_2020 = CONSUMPTION_TWH[: IDX_2019 + 1]

YEARS_2020_2024 = YEARS[IDX_2019: IDX_2024 + 1]
DATA_2020_2024 = CONSUMPTION_TWH[IDX_2019: IDX_2024 + 1]

YEARS_PROJECTED = YEARS[IDX_2024:]
DATA_PROJECTED = CONSUMPTION_TWH[IDX_2024:]

X_LIMITS = (YEARS[0], YEARS[-1])
Y_MAX = max(CONSUMPTION_TWH) * 1.05
X_MARGIN = 0.5


def _apply_axis_formatting() -> None:
	plt.xlabel("Year")
	plt.ylabel("Energy Consumption (TWh)")
	plt.xlim(X_LIMITS[0] - X_MARGIN, X_LIMITS[1] + X_MARGIN)
	plt.ylim(0, Y_MAX)
	plt.grid(alpha=0.3)
	plt.xticks(fontsize=18)
	plt.yticks(fontsize=18)
	plt.legend(loc="upper left", fontsize=18)
	plt.tight_layout()


def plot_historical_only() -> None:
	"""Plot only the historical data up to 2024."""

	plt.figure(figsize=(10, 6))
	# plt.plot(
	# 	YEARS_PRE_2020,
	# 	DATA_PRE_2020,
	# 	color="tab:blue",
	# 	linewidth=2,
	# 	marker="o",
	# 	label="2015-2019 (historical)",
	# )
	plt.plot(
		YEARS_PRE_2020 + YEARS_2020_2024,
		DATA_PRE_2020 + DATA_2020_2024,
		color="tab:blue",
		linewidth=2,
		marker="o",
		label="2015-2024 (historical)",
	)
	_apply_axis_formatting()
	plt.savefig("power_consumption_historical.png", dpi=300)


def plot_with_projection() -> None:
	"""Plot the historical data plus projections from 2025 onward."""

	plt.figure(figsize=(10, 6))
	# plt.plot(
	# 	YEARS_PRE_2020,
	# 	DATA_PRE_2020,
	# 	color="tab:blue",
	# 	linewidth=2,
	# 	marker="o",
	# 	label="2015-2019 (historical)",
	# )
	plt.plot(
		YEARS_PRE_2020 + YEARS_2020_2024,
		DATA_PRE_2020 + DATA_2020_2024,
		color="tab:blue",
		linewidth=2,
		marker="o",
		label="2015-2024 (historical)",
	)
	plt.plot(
		YEARS_PROJECTED,
		DATA_PROJECTED,
		color="tab:blue",
		linewidth=2,
		linestyle="--",
		marker="o",
		label="2025-2030 (projected)",
	)
	_apply_axis_formatting()
	plt.savefig("power_consumption_with_projection.png", dpi=300)


def plot_country_comparison() -> None:
	"""Plot a horizontal bar chart comparing country-level consumption."""

	sorted_items = sorted(
		COUNTRY_CONSUMPTION_TWH.items(), key=lambda item: item[1], reverse=False
	)
	countries, values = zip(*sorted_items)

	fig, (ax_close, ax_far) = plt.subplots(
		1,
		2,
		sharey=True,
		figsize=(8, 10),
		gridspec_kw={"width_ratios": [3, 1]},
	)

	bar_kwargs = {"color": "tab:blue"}
	for ax in (ax_close, ax_far):
		ax.barh(countries, values, **bar_kwargs)
		ax.invert_yaxis()
		ax.grid(axis="x", alpha=0.3, linestyle=":")
		ax.set_facecolor("white")
		ax.tick_params(axis="y", labelsize=24)
		ax.tick_params(axis="x", labelsize=16)
    

	# ax_close.set_xlabel("Energy Consumption (TWh)", fontsize=22)
	ax_close.set_xlim(0, 1800)
	ax_far.set_xlim(3500, max(values) + 500)

	ax_far.yaxis.set_visible(False)
	ax_far.spines["left"].set_visible(False)
	ax_close.spines["right"].set_visible(False)

	d = 0.02
	kwargs = dict(transform=ax_close.transAxes, color="k", clip_on=False)
	ax_close.plot((1, 1), (-d, +d), **kwargs)
	ax_close.plot((1, 1), (1 - d, 1 + d), **kwargs)
	kwargs.update(transform=ax_far.transAxes)
	ax_far.plot((0, 0), (-d, +d), **kwargs)
	ax_far.plot((0, 0), (1 - d, 1 + d), **kwargs)

	plt.tight_layout()
	plt.savefig("power_consumption_countries.png", dpi=300)


def main() -> None:
	"""Render both projections per user specification."""

	plot_historical_only()
	plot_with_projection()
	plot_country_comparison()


if __name__ == "__main__":
	main()