# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.18.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # <div align=center>**Placeholder**</div>


# %% [markdown]
# ## Setup
# ---

# %%
from pathlib import Path
from typing import cast

import matplotlib.pyplot as plt
import pandas as pd
import requests
from matplotlib.axes import Axes
from matplotlib.container import BarContainer

# %%
url = "https://data.scryfall.io/unique-artwork/unique-artwork-20251220100350.json"
filename = Path("unique-artwork.json")
directory = Path("data")
file = directory / filename
directory.mkdir(exist_ok=True)
if not (file).is_file():
    response = requests.get(url)
    response.raise_for_status()
    file.write_bytes(response.content)
base_df = pd.read_json(file)

# %%
pd.set_option("display.max_columns", None)

# %% [markdown]
# ## Quick overview
# ---

# %%
base_df.info()

# %% [markdown]
# ## Placeholder title
# ---

# %%
df = base_df["artist"].value_counts().head(10).iloc[::-1]
ax: Axes = df.plot(kind="barh", color="dodgerblue", edgecolor="black", width=0.8)
for side in ["bottom", "right", "top", "left"]:
    ax.spines[side].set_visible(False)
ax.set_xticklabels([])
ax.set_xticks([])
ax.bar_label(
    cast(BarContainer, ax.containers[0]),
    label_type="center",
    color="white",
    weight="bold",
)
ax.tick_params(left=False)
plt.title("Top 10 artists by artworks")
plt.xlabel("")
plt.ylabel("")
plt.show()
