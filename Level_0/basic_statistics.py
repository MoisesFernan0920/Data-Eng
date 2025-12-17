import pandas as pd 

# Review of Python and Pandas to perform basic statistics (mean, median, std)

# Sample data 
names = ["Alice","Bob","Charlie","Diana","Ethan"]
age = [25,30,28,22,31]
height = [165,175,170,160,180]
weight = [68,82,75,62,85]

# Create a DataFrame 
data = pd.DataFrame({
    "Name" : names, 
    "Age" : age,
    "Height (cm)": height,
    "Weight (kg)": weight 
})

# Display the DataFrame 
print(data)

# Calculate mean, median, and standard deviation (Age)
mean_age = data["Age"].mean()
median_age = data["Age"].median()
std_age = data["Age"].std()

# Displays Calculated Statistics for Age 
print("\nStatistics for Age:")
print(f"Mean: {mean_age}")
print(f"Median: {median_age}")
print(f"Standard Deviation : {std_age}")

# Calculate mean, median, and standard deviation (Height)
mean_height = data["Height (cm)"].mean()
median_height = data["Height (cm)"].median() 
std_height = data["Height (cm)"].std()

# Displays Calculated Statistics for Height 
print("\nStatistics for Height:")
print(f"Mean: {mean_height}")
print(f"Median: {median_height}")
print(f"Standard Deviation : {std_height}")

# Calculate mean, median, and standard deviation (Weight)
mean_weight = data["Weight (kg)"].mean()
median_weight = data["Weight (kg)"].median()
std_weight = data["Weight (kg)"].std()

# Displays Calcualted Statistics for Weight 
print("\nStatistics for Weight:")
print(f"Mean: {mean_weight}")
print(f"Median: {median_weight}")
print(f"Standard Deviation : {std_weight}")

