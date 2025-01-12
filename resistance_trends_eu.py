import pandas as pd
import matplotlib.pyplot as plt

# Path to the CSV file
file_path = "ECDC_surveillance_data_Antimicrobial_resistance_all EU countries.csv"

# Load the CSV file
df = pd.read_csv(file_path)

# Initialize and array to store the years where the percentage exceeds the threshold
highlight_years = []

# Define the threshold
threshold = 30

# Loop through the data
for index, row in df.iterrows(): 
    year = row['Time']
    value = row['NumValue']
    
    # Decision: Check if the value exceeds the threshold
    if value > threshold:
        highlight_years.append(year)

# Create a line graph
plt.figure(figsize=(10, 6))
plt.plot(df['Time'], df['NumValue'], marker='o', linestyle='-')

# Highlight the points that exceed the threshold
for year in highlight_years:
    plt.axvline(x=year, color='r', linestyle='--', alpha=0.7)
    
# Calculate the year-to-year change
df['Change'] = df['NumValue'].diff()

# Find the years with less than 1% change
constant_years = df[df['Change'] <1]['Time'].tolist()

# Highlight the years with less than 1% change
for year in constant_years: 
    plt.axvline(x=year, color='g', linestyle='--', alpha=0.7)

# Add ticks if NumValue exceeds 30%
for index, row in df.iterrows():
    if row['NumValue'] > 30:
        plt.plot(row['Time'], row['NumValue'], marker='x', color='y')
    else:
        plt.plot(row['Time'], row['NumValue'], marker='o', color='b')

# Set the title and labels
plt.title('Percentage K. pneumoniae carbapenem resistant isolates over time in Bulgaria')
plt.xlabel('Year')
plt.ylabel('Percentage Resistant Isolates')
plt.xticks(df['Time'], rotation=45)
plt.gca().xaxis.set_major_locator(plt.MaxNLocator(integer=True))

# Step 4: Customize and save the plot
plt.grid(True)
plt.tight_layout()

# Save the plot
plt.savefig("resistance_trends.png")
plt.show()
