import pandas as pd 

# Load the data 
data = pd.read_csv("laptopData.csv")
print(data.info())

# Intial Data Inspection 
print("Initial data shape: ", data.shape)

print("Missing values in each column BEFORE cleaning: ")
print(data.isnull().sum())

print("Number of duplicate rows BEFORE cleaning: ")
print(data.duplicated().sum())

# Handle Missing Values 
# Nan = Not a Number (#)
data.replace("?", pd.NA, inplace = True)

# Dropped any with missing data 
critical_cols = ["Company","Cpu","Ram","Memory","Gpu","OpSys","Weight","Price"] # missing two 
data = data.dropna(subset = critical_cols)

# Drop duplicates 
data = data.drop_duplicates()
print(" Cleaned data shape:", data.shape)

# Standardize our columns (convert strings (objects) into numbers (float64 or int64) )
data["Weight"] = data["Weight"].str.replace("kg","", regex = False)
data["Weight"] = pd.to_numeric(data["Weight"], errors = "coerce")

data["Price"] = pd.to_numeric(data["Price"], errors = "coerce")

# Windows 10 -> windows_10 
data["OpSys"] = data["OpSys"].str.lower().str.replace(" ", "_")

# print(data.head())

# extract CPU speed from the "Cpu" column 
def extract_cpu(cpu_info):
    try: 
        return float(cpu_info.split()[-1][:-3]) # 2.7 
    except Exception as e: 
        return None 

# Create new column in our dataset for this new CPU Data 
data["Cpu_Speed"] = data["Cpu"].apply(extract_cpu)
# print("Current data shape:", data.shape)

def convert_memory(memory):
    try: 
        if "GB" in memory: 
            return int(memory.replace("GB","")) * 1024 # MB 
        elif "TB" in memory: 
            return int(memory.replace("TB","")) * 1024 * 1024 
    except Exception as e: 
        return None 
    
data["Memory_MB"] = data["Memory"].apply(convert_memory)

# Replace any NaN with the Average of that column 
# fillna() 

data["Weight"].fillna(data["Weight"].mean(), inplace = True)
data["Price"].fillna(data["Price"].mean(), inplace = True)
data["Cpu_Speed"].fillna(data["Cpu_Speed"].mean(), inplace = True)
data["Memory_MB"].fillna(data["Memory_MB"].mean(), inplace = True)

# Final Testing 
print("Final data shape:", data.shape)

print("Missing values in each column AFTER cleaning: ")
print(data.isnull().sum())

print("Number of duplicate rows AFTER cleaning: ")
print(data.duplicated().sum())

print("All the Data Types")
print(data.dtypes)

print(data.info())
