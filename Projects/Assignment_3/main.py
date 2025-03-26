import polars as pl 
import matplotlib.pyplot as plt 

# Load Data 
data = pl.read_csv("coral.csv")

# Initial Inspection 
print("DataFrame shape: ", data.shape)
print("Num of missing values", data.null_count())
print("Num of duplicate values:", data.is_duplicated().sum())

# Critical columns 
critical_cols = ["Reef ID", "Reef Name", "Longitude Degrees", "Latitude Degrees", "Country", "Depth", "Organism Code", "S1", "S2", "S3", "S4"]

# Data cleaning 
data = data.drop_nulls(subset=critical_cols).unique()

data = data.with_columns(
    (pl.col("Longitude Degrees").cast(pl.Utf8) + " " + pl.col("Longitude Minutes").cast(pl.Utf8) + " " +
    pl.col("Longitude Seconds").cast(pl.Utf8) + " " + pl.col("Longitude Cardinal Direction")).alias("Longitude"),
    (pl.col("Latitude Degrees").cast(pl.Utf8) + " " + pl.col("Latitude Minutes").cast(pl.Utf8) + " " +
    pl.col("Latitude Seconds").cast(pl.Utf8) + " " + pl.col("Latitude Cardinal Direction")).alias("Latitude"),
    pl.col("Depth").cast(pl.Float64).fill_null(strategy="mean"),
    pl.col("Year").cast(pl.Int32)
)

data = data.drop_nulls(subset=["Year"])

# Compute Bleaching Percentage 
data = data.with_columns(
    (pl.col("S1") + pl.col("S2") + pl.col("S3") + pl.col("S4")).alias("Bleaching_Percentage")
)

data = data.with_columns(
    pl.col("Bleaching_Percentage").fill_null(strategy="mean").clip_upper(100)
)

# Filtering Data 
data_reef_depth = data.filter(pl.col("Depth") > 5)
data_high_bleaching = data.filter(pl.col("Bleaching_Percentage")> 50)
data_years = data.filter(pl.col("Year") >= 2000)

# Grouping Data 
bleaching_by_country = data.group_by("Country").agg([
    pl.col("Bleaching_Percentage").mean().alias("mean"),
    pl.col("Bleaching_Percentage").std().alias("std")
]).sort("mean",descending= True).head(15)

pivot = data.pivot_table(values = "Bleaching_Percentage", index = "Country", columns = "Year", aggregate_function = "mean")
pivot = pivot.select(["Country"] + [str(year) for year in range(2007, 2018)])
top_countries = pivot.with_columns(pivot.select(pl.exclude("Country")).mean_horizontal().alias("avg")).sort("avg", descending=True).head(15)["Country"]
pivot = pivot.filter(pl.col("Country").is_in(top_countries))

# Data Visualization 
fig, axs = plt.subplots(2,2,figsize = (18,12))

# 1 - Highest Average Bleaching by Country 
axs[0,0].bar(bleaching_by_country["Country"], bleaching_by_country["mean"], color = "purple")
axs[0,0].set_title("Average Bleaching by Country")
axs[0,0].set_ylabel("Average Bleaching")
axs[0,0].errorbar(bleaching_by_country["Country"], bleaching_by_country["mean"], yerr = bleaching_by_country["std"], fmt = "none", c = "black", capsize = 5, label = "Standard Deviation")
axs[0,0].legend()

# 2 - Number of Reefs by Depth 
depth_count = data_reef_depth["Depth"].cast(pl.Int32).value_counts().sort("Depth")
axs[0,1].scatter(depth_count["Depth"], depth_count["counts"], color = "red")
axs[0,1].set_title("Number of reefs by depth")
axs[0,1].set_xlabel("Depth")
axs[0,1].set_ylabel("Count")

# 3 - Bleaching Percentage by country (2007 - 2017)
pivot.drop("Country").transpose().plot(kind = "bar", ax = axs[1,0], width = 0.8)
axs[1,0].set_title("Bleaching by Year and Country")
axs[1,0].set_ylabel("Bleaching Percentage")

# 4 - Top 15 Bleaching Location 
top_bleaching = data_high_bleaching.head(15)
axs[1,1].bar(top_bleaching["Reef Name"], top_bleaching["Bleaching_Percentage"])
axs[1,1].set_title("Top 15 Bleaching Locations")
axs[1,1].set_ylabel("Percentage")

plt.tight_layout() 
plt.show()
