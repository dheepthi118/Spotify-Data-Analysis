# Spotify Music Insights — Exploratory Data Analysis

## Project Overview

This project explores a Spotify tracks dataset using Python to discover patterns in music popularity, release trends, and audio features. Data visualization techniques are used to present findings clearly and identify relationships between numerical music attributes.

## Objectives

- Analyze the distribution of Spotify track popularity.
- Explore music release trends across different years.
- Compare average track popularity by release year.
- Examine track mode and time signature distributions.
- Investigate correlations between audio features.
- Present insights through clear, professional visualizations.

## Technologies Used

- **Python** — Data analysis
- **Pandas** — Data manipulation and analysis
- **Matplotlib** — Data visualization
- **Seaborn** — Statistical charts and heatmaps

## Project Structure

```text
Spotify-Music-Insights/
├── data/
│   └── spotify_tracks.csv
├── visualizations/
│   ├── 01_popularity_distribution.png
│   ├── 02_release_year_trends.png
│   ├── 03_popularity_over_time.png
│   ├── 04_track_modes.png
│   ├── 05_time_signatures.png
│   └── 06_audio_feature_correlation.png
├── eda_analysis.py
├── report.md
└── README.md
```

*Note: Some visualizations may be absent if the required columns are unavailable or the relevant data is insufficient.*

## Visualizations

The project generates the following charts:

1. **Popularity Distribution** — Examines how track popularity scores are distributed.
2. **Release Year Trends** — Shows the number of tracks associated with each release year.
3. **Popularity Over Time** — Compares average popularity across release years.
4. **Track Modes** — Displays the distribution of track modes.
5. **Time Signatures** — Compares the frequency of time signatures.
6. **Audio Feature Correlation** — Uses a heatmap to explore relationships between numerical audio features.

All generated charts are saved in the `visualizations/` directory.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/Spotify-Music-Insights.git
cd Spotify-Music-Insights
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Install the required libraries

```bash
pip install pandas matplotlib seaborn
```

### 3. Run the analysis

Make sure `spotify_tracks.csv` is inside the `data/` folder, then run:

```bash
python eda_analysis.py
```

The script analyzes the dataset, displays the visualizations, and saves the generated charts to the `visualizations/` directory.

## Key Findings

Findings will be documented after examining the actual dataset output and visualizations, including popularity patterns, release trends, and notable correlations.

## Limitations

- Results depend on the quality and coverage of the dataset.
- Popularity scores may change over time.
- Correlation does not imply causation.
- Findings
