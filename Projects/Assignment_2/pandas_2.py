import pandas as pd 

# Create a dataframe 
df = pd.read_csv("data_set.csv")

# Simple Inspection 
print(df.info())
print(df.head())
print(df.tail())


# Scenario 1 
# Question : How many cities are there in each country 
# Hint - Group by Country and Count Cities 
country_group = df.groupby(by = 'Country')["City"].count()
# print("Total: ", country_group)


# Scenario 2 
# Question : What is the average population for each country in 2024 
# Hint - Group by Country and Calculate Average Population
country_average = df.groupby(by = 'Country')["Population (2024)"].mean()
# print("Average: ", country_average)

# Scenario 3 
# Question : What is the total growth rate for each country 
# Hint - Group by Country and Calculate Total Growth Rate 

# Positive Growth Rate value -> Country is actually growing 
growing_countries = df[df["Growth Rate"] > 0 ]

# Adding the growth rates of each country 
country_growth = growing_countries.groupby("Country")["Growth Rate"].sum().reset_index() 
# print(country_growth)

# Scenario 4 
# Question : What is the average population for each combination of country and growth rate in 2024 
# Hint - Group by Country and Growth Rate, then Calculate Average Population 
country_average_growthrate = df.groupby(by = ['Country','Growth Rate'])["Population (2024)"].mean().reset_index()
print("Total: ", country_average_growthrate)

# Scenario 5 
# Question : What are the summary statistics (mean, sum, max, min) for the population in 2024 for each country? 
# Hint - Group by Country and Get Summary Statistics for Population 
country_stats = df.groupby("Country")["Population (2024)"].aggregate["mean","sum","max","min"]
print(country_stats)

# Scenario 6 
# Question : How many cities fall into each growth rate catergory within each country 
# Hint - Group by Country and Population Growth rate Catergories 
# High Growth, Moderate, Negative 

def growth_catergory(growth): 
    if growth > 0.02: 
        return "High Growth"
    elif growth > 0: 
        return "Moderate Growth"
    else:
        return  "Negative Growth"
    
df["Growth Catergory"] = df["Growth Rate"].apply(growth_catergory)

growth_count = df.groupby(by = ["Country", "Growth Catergory"])["City"].count()

print(growth_count)