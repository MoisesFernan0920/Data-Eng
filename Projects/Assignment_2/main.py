# Questions for  Analysis 
# 1 - Which countries have the highest average bleaching percentage ? 
# 2 - How does the variability (standard deviation) of bleaching percentages compare across different countries ? 
# 3 - What is the distribution of reef depths in our dataset? 
# 4 - How has the bleaching percentage changed over the years from 2007 to 2017 in the top countries ? 
# 5 - Which reefs have the highest bleaching percentages ? 
 
#################################################################################################################

import pandas as pd 
import matplotlib.pyplot as plt

data = pd.read_csv("coral.csv")

print(data.info())

# Initial Inspection 
print("Dataframe shape:", data.shape)
print("Num of missing values:", data.isnull().sum()) 
print("Num of duplicate values:", data.duplicated().sum())

critical_cols = ["Reef ID", "Reef Name", "Longitude Degrees","Latitude Degrees", "Country", "Depth", "Organism Code", "S1", "S2","S3","S4"]

# To check for coral bleaching it is a combination between the S1, S2, S3, and S4 values -> adding these together and seeing which reefs have the highest value are the ones
# with the highest amount of coral bleaching 

# Drops any data entries without the specified columns or duplicated values -> inital data cleaning steps 
data = data.dropna(subset = critical_cols)
data = data.drop_duplicates() 

#################################################################################################################
# Standarizing the data 

data["Longitude"] = (
    data["Longitude Degrees"].astype(str) + " " 
    + data["Longitude Minutes"].astype(str) + " " 
    + data["Longitude Seconds"].astype(str) + " " 
    + data["Longitude Cardinal Direction"]
)

data["Latitude"] = (
    data["Latitude Degrees"].astype(str) + " " 
    + data["Latitude Minutes"].astype(str) + " " 
    + data["Latitude Seconds"].astype(str) + " " 
    + data["Latitude Cardinal Direction"]
)

data["Depth"] = pd.to_numeric(data["Depth"], errors="coerce")
data["Depth"] = data["Depth"].fillna(data["Depth"].mean())

data["Year"] = pd.to_numeric(data["Year"], errors="coerce")
data = data.dropna(subset=["Year"])

# Function to get the bleaching value 
def extract_bleaching(row):
    return row["S1"] + row["S2"] + row["S3"] + row["S4"]

# Extracting the Bleaching value and making a column -> Empty columns will have the mean as a fill in value 
data["Bleaching_Percentage"] = data.apply(extract_bleaching, axis=1)
data["Bleaching_Percentage"] = data["Bleaching_Percentage"].fillna(data["Bleaching_Percentage"].mean())
data["Bleaching_Percentage"] = data["Bleaching_Percentage"].apply(lambda x: min(x, 100)) # Cap at 100% -> since this means the reef is fully dead so there will be no point in counting it 

#################################################################################################################
# Filtering and Grouping Data 
# Filters 
# 1 - Reef depth value 
# 2 - Bleaching Percentage 
# 3 - Year 

data_reef_depth = data[data["Depth"]>5] 
data_high_bleaching = data[data["Bleaching_Percentage"] > 50]
data_years  = data[data["Year"] >= 2000]


group_by_country = data.groupby("Country")["Bleaching_Percentage"].aggregate(["mean", "std"]).sort_values(by = 'mean', ascending = False).head(15)

pivot = data.pivot_table(values = 'Bleaching_Percentage', index = 'Country', columns = 'Year', aggfunc = 'mean')
pivot = pivot.loc[:, 2007:2017]
top_countries = pivot.mean(axis = 1).sort_index(ascending = False).head(15).index
pivot = pivot.loc[top_countries]
print(pivot)

#################################################################################################################
# Data Visualization 

fig, axs = plt.subplots(2,2,figsize = (18,12))

# 1 - Which countries have the highest average bleaching percentage ? 
group_by_country['mean'].plot(kind = 'bar', ax = axs [0,0], color = 'purple')
axs[0,0].set_title("Average Bleaching by Country")
axs[0,0].set_ylabel("Average Bleaching")
axs[0,0].errorbar(group_by_country.index,group_by_country["mean"], yerr = group_by_country['std'], fmt = 'none', c = 'black', capsize = 5, label = "Standard Deviation")
axs[0,0].legend()

# 2- Number of Reefs by Depth 
depth_count = data_reef_depth["Depth"].astype(int).value_counts().sort_index()
axs[0,1].scatter(depth_count.index, depth_count.values, color = 'red') 
axs[0,1].set_title("Number of reefs by depth ")
axs[0,1].set_xlabel("Depth")
axs[0,1].set_ylabel("Count")

# 3 - Bleaching Percentage by country (2007-2017)
pivot.plot(kind = "bar", ax = axs[1,0], width = 0.8)
axs[1,0].set_title("Bleaching by Year and Country")
axs[1,0].set_ylabel("Bleaching Percentage")

# 4 - Top 15 places for bleaching
data_high_bleaching.head(15).set_index("Reef Name")["Bleaching_Percentage"].plot(kind = 'bar', ax = axs[1,1])
axs[1,1].set_title("Top 15 Bleaching Locations")
axs[1,1].set_ylabel("Percentage")

plt.tight_layout()
plt.show()




