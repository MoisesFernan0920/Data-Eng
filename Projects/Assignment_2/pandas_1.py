import pandas as pd 

# Create  a dataframe 
df = pd.read_csv("data_set.csv")

# Basic Pandas Operations 

print(df.info)
print(df.tail())
print(df.head())
print(df.describe())



# Scenario 1 
# Find cities with a population greater than 20 million 
largest_cities = df[df["Population (2024)"]> 20000000]
# print("Cities with population larger than 20 million:", largest_cities)


# Scenario 2 
# Find all the largest cities in Vietnam 
vietnam = df[df["Country"] == "Vietnam"]
# print("Largest cities in Vietnam: ", vietnam)

# Scenario 3 
# Find Cities in China  that are growing in population 2024 (positive growth)
growing_cities_china = df[(df["Country"]== "China") & (df["Growth Rate"]> 0)]
# print("Growing cities in China : ", growing_cities_china)

# Scenario 4 
# Calculate the total population of the largest cities in India 
cities_india = df[df["Country"] == "India"]["Population (2024)"].sum()
# print("Sum of Largest cities in India: ", cities_india)


# Scenario 5 
# Find cities experiencing a population decline and calculate their growth median 
population_decline_median = df[df["Growth Rate"] < 0]["Growth Rate"].median()
# print("Decline Median Cities: ", population_decline_median)


# Scenario 6 
# Find the growing cities in China and calculate the minimum population they had in 2023 
min_pop_china_2023 = df[(df["Country"] == "China") & (df["Growth Rate"] > 0)]["Population (2023)"].min()
# print("Min pop in China for 2023", min_pop_china_2023)

