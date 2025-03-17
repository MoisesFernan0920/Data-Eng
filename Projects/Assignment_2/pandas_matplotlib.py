import pandas as pd 
import matplotlib.pyplot as plt

# Load the dataset 
df = pd.read_csv('airbnb.csv')

# Initial Exploration 
print(df.head())
print(df.info())
print("Initial Data Shape:", df.shape)
print(df.describe())

# Identify missing values and duplicates 
print("Missing values:\n", df.isnull().sum())
print("Number of duplicates:", df.duplicated().sum)

# Handle missing values by filtering with the average 
df["reviews_per_month"].fillna(df.duplicated().sum())
df["price"].fillna(df['price'].mean(), inplace = True)
df["number_of_reviews"].fillna(df['number_of_reviews'].mean(), inplace = True)

# Drop rows where data is still missing & duplicates 
df.dropna(inplace = True)
df.drop_duplicates(inplace = True)

# AFTER ther Initial Cleaning 
print(df.head())
print(df.info())
print("Initial Data Shape:", df.shape)
print(df.describe())

# Data Visualization 
df["price"].plot()
plt.ylabel("Price")
plt.title("Plot of Prices")
plt.show()

df.plot(kind = 'scatter', x ='price', y = 'number_of_reviews', color = "purple")
plt.title("Price vs Num of Reviews")
plt.show()


# Power of Subplots 
fig, axs = plt.subplots(2,3,figsize = (15,10))


# Price vs. Frequency 
axs[0,0].hist(df['price'], bins = 20, color = 'lightblue')
axs[0,0].set_title("Price vs Frequency")
axs[0,0].set_xlabel("Price")
axs[0,0].set_ylabel("Frequency")

# Number of Reviews vs Frequency 
axs[0,1].hist(df['number_of_reviews'], bins = 20, color = 'red')
axs[0,1].set_title("Number of Reviews vs Frequency")
axs[0,1].set_xlabel("Numbers of Reviews")
axs[0,1].set_ylabel("Frequency")

# Group by type of room and show average price -> use breaks here 
room_type = df.groupby('room_type')['price'].mean().reset_index()
axs[0,2].bar(room_type['room_type'],room_type['price'], color = 'lightgreen')
axs[0,2].set_title("Average Price by Room Type")
axs[0,2].set_xlabel("Room Type")
axs[0,2].set_ylabel("Price")

# Number of listings in each borough (NYC) -> use breaks here 
neighborhoods = df["neighbourhood_group"].value_counts().reset_index() 
neighborhoods.columns = ['neighbourhood_group', 'count']

axs[1,0].bar(neighborhoods["neighbourhood_group"], neighborhoods['count'], color = "orange")
axs[1,0].set_title("Listing by Neighborhood")
axs[1,0].set_xlabel("Neighborhood")
axs[1,0].set_ylabel("Number of Listing")

# Price vs Number of Reviews 
axs[1,1].scatter(df['price'], df['number_of_reviews'], color = "blue")
axs[1,1].set_title("Price vs. Reviews")
axs[1,1].set_xlabel("Price")
axs[1,1].set_ylabel("Number of Reviews")

plt.tight_layout
plt.show()


