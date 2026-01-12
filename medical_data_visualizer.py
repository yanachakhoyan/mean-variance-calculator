import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1) Import data
df = pd.read_csv("medical_examination.csv")

# 2) Add overweight column (BMI > 25 => 1 else 0)
df["overweight"] = ((df["weight"] / ((df["height"] / 100) ** 2)) > 25).astype(int)

# 3) Normalize cholesterol and gluc: 0 good, 1 bad
df["cholesterol"] = (df["cholesterol"] > 1).astype(int)
df["gluc"] = (df["gluc"] > 1).astype(int)


def draw_cat_plot():
    # 4-6) Melt + group counts + catplot
    df_cat = pd.melt(
        df,
        id_vars=["cardio"],
        value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"],
    )

    df_cat = (
        df_cat.groupby(["cardio", "variable", "value"])
        .size()
        .reset_index(name="total")
    )

    fig = sns.catplot(
        data=df_cat,
        x="variable",
        y="total",
        hue="value",
        col="cardio",
        kind="bar",
    ).fig

    # 8) Do not modify next two lines
    fig.savefig("catplot.png")
    return fig


def draw_heat_map():
    # 10-11) Clean data
    df_heat = df[
        (df["ap_lo"] <= df["ap_hi"])
        & (df["height"] >= df["height"].quantile(0.025))
        & (df["height"] <= df["height"].quantile(0.975))
        & (df["weight"] >= df["weight"].quantile(0.025))
        & (df["weight"] <= df["weight"].quantile(0.975))
    ]

    # 12) Correlation
    corr = df_heat.corr()

    # 13) Mask upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14) Matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 12))

    # 15) Heatmap
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt=".1f",
        square=True,
        center=0,
        cbar_kws={"shrink": 0.5},
        ax=ax,
    )

    # 16) Do not modify next two lines
    fig.savefig("heatmap.png")
    return fig
