import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import data (make sure the file is named exactly this)
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=["date"], index_col="date")

# Clean data
low = df["value"].quantile(0.025)
high = df["value"].quantile(0.975)
df = df[(df["value"] >= low) & (df["value"] <= high)]


def draw_line_plot():
    # Use a copy
    df_line = df.copy()

    fig, ax = plt.subplots(figsize=(12, 4))
    ax.plot(df_line.index, df_line["value"])
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    fig.savefig("line_plot.png")
    return fig


def draw_bar_plot():
    # Use a copy
    df_bar = df.copy()
    df_bar["year"] = df_bar.index.year
    df_bar["month"] = df_bar.index.month_name()

    # Average daily page views for each month grouped by year
    df_bar = df_bar.groupby(["year", "month"])["value"].mean().reset_index()

    # Ensure months are in correct order
    month_order = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    df_bar["month"] = pd.Categorical(df_bar["month"], categories=month_order, ordered=True)

    df_bar_pivot = df_bar.pivot(index="year", columns="month", values="value")

    fig = df_bar_pivot.plot(kind="bar", figsize=(12, 8)).figure
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(title="Months")

    fig.savefig("bar_plot.png")
    return fig


def draw_box_plot():
    # Prepare data (use a copy)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box["year"] = df_box["date"].dt.year
    df_box["month"] = df_box["date"].dt.strftime("%b")
    df_box["month_num"] = df_box["date"].dt.month

    # Sort months
    df_box = df_box.sort_values("month_num")

    fig, axes = plt.subplots(1, 2, figsize=(20, 6))

    # Year-wise box plot
    sns.boxplot(data=df_box, x="year", y="value", ax=axes[0])
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")

    # Month-wise box plot
    sns.boxplot(data=df_box, x="month", y="value", ax=axes[1])
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    fig.savefig("box_plot.png")
    return fig
