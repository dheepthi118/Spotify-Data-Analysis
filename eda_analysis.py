
import pandas as pd
import os

# Load the Spotify dataset
file_path = os.path.join("data", "spotify_tracks.csv")
df = pd.read_csv(file_path)

# Display basic dataset information
print("SPOTIFY TRACKS - EXPLORATORY DATA ANALYSIS")
print("=" * 45)

print("\nFirst 5 rows:")
print(df.head())

print("\nDataset shape (rows, columns):")
print(df.shape)

print("\nColumn names:")
print(df.columns.tolist())

print("\nDataset information:")
df.info()

print("\nMissing values in each column:")
print(df.isnull().sum())

print("\nNumber of duplicate rows:")
print(df.duplicated().sum())

print("\nNumerical column statistics:")
print(df.describe())

# ============================================
# PROFESSIONAL SPOTIFY DATA VISUALIZATIONS
# ============================================

import matplotlib.pyplot as plt
import seaborn as sns
import os
import pandas as pd

# Create output folder
os.makedirs("visualizations", exist_ok=True)

# Professional chart styling
sns.set_theme(style="whitegrid", context="notebook")
plt.rcParams["figure.figsize"] = (12, 6)
plt.rcParams["axes.titleweight"] = "bold"
plt.rcParams["axes.titlesize"] = 17
plt.rcParams["axes.labelsize"] = 12
plt.rcParams["font.family"] = "DejaVu Sans"

print("\nCreating professional Spotify visualizations...")

# --------------------------------------------
# 1. TRACK POPULARITY DISTRIBUTION
# --------------------------------------------

if "popularity" in df.columns:
    popularity = pd.to_numeric(df["popularity"], errors="coerce").dropna()

    fig, ax = plt.subplots(figsize=(12, 6))

    sns.histplot(
        popularity,
        bins=25,
        kde=True,
        color="#1DB954",
        edgecolor="white",
        linewidth=1,
        ax=ax
    )

    ax.axvline(
        popularity.mean(),
        color="#E76F51",
        linestyle="--",
        linewidth=2,
        label=f"Average: {popularity.mean():.1f}"
    )

    ax.set_title("How Popular Are Spotify Tracks?", pad=18)
    ax.set_xlabel("Track Popularity Score")
    ax.set_ylabel("Number of Tracks")
    ax.legend(frameon=True)
    sns.despine()

    plt.tight_layout()
    plt.savefig(
        "visualizations/01_popularity_distribution.png",
        dpi=300,
        bbox_inches="tight"
    )
    plt.show()
    plt.close()


# --------------------------------------------
# 2. MUSIC RELEASE TRENDS OVER TIME
# --------------------------------------------

if "release_year" in df.columns:
    years = pd.to_numeric(df["release_year"], errors="coerce")
    yearly_counts = years.dropna().astype(int).value_counts().sort_index()

    fig, ax = plt.subplots(figsize=(13, 6))

    ax.plot(
        yearly_counts.index,
        yearly_counts.values,
        color="#6C63FF",
        linewidth=2,
        alpha=0.8
    )

    ax.fill_between(
        yearly_counts.index,
        yearly_counts.values,
        color="#6C63FF",
        alpha=0.15
    )

    ax.set_title("Spotify Tracks Across Release Years", pad=18)
    ax.set_xlabel("Release Year")
    ax.set_ylabel("Number of Tracks")
    ax.grid(axis="y", alpha=0.3)
    sns.despine()

    plt.tight_layout()
    plt.savefig(
        "visualizations/02_release_year_trends.png",
        dpi=300,
        bbox_inches="tight"
    )
    plt.show()
    plt.close()


# --------------------------------------------
# 3. AVERAGE POPULARITY OVER THE YEARS
# --------------------------------------------

if {"release_year", "popularity"}.issubset(df.columns):
    trend_df = df[["release_year", "popularity"]].copy()

    trend_df["release_year"] = pd.to_numeric(
        trend_df["release_year"], errors="coerce"
    )
    trend_df["popularity"] = pd.to_numeric(
        trend_df["popularity"], errors="coerce"
    )
    trend_df = trend_df.dropna()

    trend_df["release_year"] = trend_df["release_year"].astype(int)

    yearly_popularity = trend_df.groupby("release_year").agg(
        average_popularity=("popularity", "mean"),
        track_count=("popularity", "size")
    )

    # Avoid misleading averages from years with very few tracks
    yearly_popularity = yearly_popularity[
        yearly_popularity["track_count"] >= 10
    ]

    if not yearly_popularity.empty:
        fig, ax = plt.subplots(figsize=(13, 6))

        ax.plot(
            yearly_popularity.index,
            yearly_popularity["average_popularity"],
            color="#E76F51",
            linewidth=2.5,
            marker="o",
            markersize=4
        )

        ax.set_title(
            "Average Track Popularity by Release Year",
            pad=18
        )
        ax.set_xlabel("Release Year")
        ax.set_ylabel("Average Popularity Score")
        ax.grid(axis="y", alpha=0.3)
        sns.despine()

        plt.tight_layout()
        plt.savefig(
            "visualizations/03_popularity_over_time.png",
            dpi=300,
            bbox_inches="tight"
        )
        plt.show()
        plt.close()


# --------------------------------------------
# 4. TRACK MODE DISTRIBUTION
# --------------------------------------------

if "mode" in df.columns:
    mode_counts = df["mode"].dropna().value_counts().sort_index()

    fig, ax = plt.subplots(figsize=(9, 5))

    bars = ax.bar(
        mode_counts.index.astype(str),
        mode_counts.values,
        color=["#1DB954", "#6C63FF"][:len(mode_counts)],
        width=0.55
    )

    ax.bar_label(bars, padding=4, fontsize=11)

    ax.set_title("Distribution of Track Modes", pad=18)
    ax.set_xlabel("Mode (as encoded in the dataset)")
    ax.set_ylabel("Number of Tracks")
    ax.grid(axis="y", alpha=0.25)
    sns.despine()

    plt.tight_layout()
    plt.savefig(
        "visualizations/04_track_modes.png",
        dpi=300,
        bbox_inches="tight"
    )
    plt.show()
    plt.close()


# --------------------------------------------
# 5. TIME SIGNATURE DISTRIBUTION
# --------------------------------------------

if "time_signature" in df.columns:
    signature_counts = (
        df["time_signature"]
        .dropna()
        .value_counts()
        .sort_index()
    )

    fig, ax = plt.subplots(figsize=(10, 5))

    bars = ax.bar(
        signature_counts.index.astype(str),
        signature_counts.values,
        color=sns.color_palette("mako", len(signature_counts)),
        width=0.65
    )

    ax.bar_label(bars, padding=3, fontsize=10)

    ax.set_title("Time Signatures Used in Spotify Tracks", pad=18)
    ax.set_xlabel("Time Signature")
    ax.set_ylabel("Number of Tracks")
    ax.grid(axis="y", alpha=0.25)
    sns.despine()

    plt.tight_layout()
    plt.savefig(
        "visualizations/05_time_signatures.png",
        dpi=300,
        bbox_inches="tight"
    )
    plt.show()
    plt.close()


# --------------------------------------------
# 6. AUDIO FEATURE CORRELATION HEATMAP
# --------------------------------------------

audio_features = [
    "popularity",
    "danceability",
    "energy",
    "loudness",
    "speechiness",
    "acousticness",
    "instrumentalness",
    "liveness",
    "valence",
    "tempo",
    "duration_ms"
]

available_features = [
    column for column in audio_features
    if column in df.columns
]

if len(available_features) >= 2:
    correlation_df = df[available_features].apply(
        pd.to_numeric, errors="coerce"
    )

    correlation = correlation_df.corr()

    fig, ax = plt.subplots(figsize=(12, 9))

    sns.heatmap(
        correlation,
        annot=True,
        fmt=".2f",
        cmap="vlag",
        center=0,
        vmin=-1,
        vmax=1,
        linewidths=0.5,
        square=True,
        annot_kws={"size": 9},
        cbar_kws={"shrink": 0.8},
        ax=ax
    )

    ax.set_title(
        "Correlation Between Spotify Audio Features",
        pad=20
    )

    plt.xticks(rotation=40, ha="right")
    plt.yticks(rotation=0)
    plt.tight_layout()

    plt.savefig(
        "visualizations/06_audio_feature_correlation.png",
        dpi=300,
        bbox_inches="tight"
    )
    plt.show()
    plt.close()


print("\n" + "=" * 45)
print("VISUALIZATION GENERATION COMPLETED!")
print("Check the 'visualizations' folder for your charts.")
print("=" * 45)
