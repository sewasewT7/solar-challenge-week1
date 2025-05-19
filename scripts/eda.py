# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from windrose import WindroseAxes
import numpy as np
from matplotlib import cm  # Import Matplotlib's colormap library
from sklearn.linear_model import LinearRegression
from scipy.stats import zscore

# Load CSV files for datasets
benin_df = pd.read_csv('../files/benin-malanville.csv')
sierra_df = pd.read_csv('../files/sierraleone-bumbuna.csv')
togo_df = pd.read_csv('../files/togo-dapaong_qc.csv')

# Inspect the data structure and summary
print("Benin Data:")
print(benin_df.head())
print(benin_df.info())  # Overview of Benin dataset structure

print("\nSierra Leone Data:")
print(sierra_df.head())
print(sierra_df.info())  # Overview of Sierra Leone dataset structure

print("\nTogo Data:")
print(togo_df.head())
print(togo_df.info())  # Overview of Togo dataset structure

# Generate descriptive statistics for each dataset
print("\nBenin Data Descriptive Statistics:")
print(benin_df.describe())
print("\nSierra Leone Data Descriptive Statistics:")
print(sierra_df.describe())
print("\nTogo Data Descriptive Statistics:")
print(togo_df.describe())

# Drop the 'Comments' column if it exists, as it is entirely null
benin_df = benin_df.drop(columns=['Comments'], errors='ignore')
sierra_df = sierra_df.drop(columns=['Comments'], errors='ignore')
togo_df = togo_df.drop(columns=['Comments'], errors='ignore')

# Check for missing values in the datasets
print("\nBenin Data - Missing Values:")
print(benin_df.isnull().sum())
print("\nSierra Leone Data - Missing Values:")
print(sierra_df.isnull().sum())
print("\nTogo Data - Missing Values:")
print(togo_df.isnull().sum())

# Fill missing values in numeric columns with the median
for df in [benin_df, sierra_df, togo_df]:
    numeric_cols = df.select_dtypes(include=['float64', 'int64'])
    df[numeric_cols.columns] = numeric_cols.fillna(numeric_cols.median())

# Verify that missing values have been handled
print("\nBenin Data - Missing Values After Handling:")
print(benin_df.isnull().sum())
print("\nSierra Leone Data - Missing Values After Handling:")
print(sierra_df.isnull().sum())
print("\nTogo Data - Missing Values After Handling:")
print(togo_df.isnull().sum())

# Convert the 'Timestamp' column to datetime format for time-based analysis
benin_df['Timestamp'] = pd.to_datetime(benin_df['Timestamp'])
sierra_df['Timestamp'] = pd.to_datetime(sierra_df['Timestamp'])
togo_df['Timestamp'] = pd.to_datetime(togo_df['Timestamp'])

# Extract time components from the 'Timestamp' column for trend analysis
benin_df['Month'] = benin_df['Timestamp'].dt.month
benin_df['Day'] = benin_df['Timestamp'].dt.day
benin_df['Hour'] = benin_df['Timestamp'].dt.hour

# Identify and remove outliers based on Z-scores (values with |Z| > 3 are considered outliers)
z_scores = benin_df.select_dtypes(include=['float64', 'int64']).apply(zscore)
benin_df_cleaned = benin_df[(z_scores.abs() < 3).all(axis=1)]

# Remove duplicate rows from all datasets
benin_df = benin_df.drop_duplicates()
sierra_df = sierra_df.drop_duplicates()
togo_df = togo_df.drop_duplicates()

# Replace negative values in wind speed (WS) and irradiance (GHI) columns with NaN
for col in ['WS', 'GHI']:
    benin_df[col] = benin_df[col].apply(lambda x: x if x >= 0 else None)
    sierra_df[col] = sierra_df[col].apply(lambda x: x if x >= 0 else None)
    togo_df[col] = togo_df[col].apply(lambda x: x if x >= 0 else None)

# Review the cleaned dataset structure and statistics
print("\nBenin Data After Cleaning:")
print(benin_df.info())
print("\nSierra Leone Data After Cleaning:")
print(sierra_df.info())
print("\nTogo Data After Cleaning:")
print(togo_df.info())

# Optionally save the cleaned datasets to new CSV files
benin_df.to_csv('benin_cleaned.csv', index=False)
sierra_df.to_csv('sierra_cleaned.csv', index=False)
togo_df.to_csv('togo_cleaned.csv', index=False)

# Plot line chart for monthly trends
monthly_data.plot(kind='line', figsize=(10, 6), marker='o')
plt.title('Monthly Trends for GHI, DNI, DHI, and Tamb')
plt.xlabel('Month')
plt.ylabel('Values')
plt.legend(loc='best')
plt.grid()
plt.show()

# Aggregate data by hour
hourly_data = benin_df.groupby('Hour')[['GHI', 'DNI', 'DHI', 'Tamb']].mean()

# Plot line chart for hourly patterns
hourly_data.plot(kind='line', figsize=(10, 6), marker='o')
plt.title('Hourly Trends for GHI, DNI, DHI, and Tamb')
plt.xlabel('Hour')
plt.ylabel('Values')
plt.legend(loc='best')
plt.grid()
plt.show()

# Group data by cleaning events
cleaning_impact = benin_df.groupby('Cleaning')[['ModA', 'ModB']].mean()

# Plot the impact of cleaning
cleaning_impact.plot(kind='bar', figsize=(8, 5), color=['blue', 'orange'])
plt.title('Impact of Cleaning on Sensor Readings (ModA and ModB)')
plt.xlabel('Cleaning Event')
plt.ylabel('Sensor Values')
plt.legend(loc='best')
plt.grid()
plt.show()


# Convert 'Timestamp' column to datetime
sierra_df['Timestamp'] = pd.to_datetime(sierra_df['Timestamp'])

# Extract time components
sierra_df['Month'] = sierra_df['Timestamp'].dt.month
sierra_df['Day'] = sierra_df['Timestamp'].dt.day
sierra_df['Hour'] = sierra_df['Timestamp'].dt.hour

# Aggregate data by month
monthly_data_sierra = sierra_df.groupby('Month')[['GHI', 'DNI', 'DHI', 'Tamb']].mean()

# Plot line chart for monthly trends
monthly_data_sierra.plot(kind='line', figsize=(10, 6), marker='o')
plt.title('Sierra Leone: Monthly Trends for GHI, DNI, DHI, and Tamb')
plt.xlabel('Month')
plt.ylabel('Values')
plt.legend(loc='best')
plt.grid()
plt.show()

# Aggregate data by hour
hourly_data_sierra = sierra_df.groupby('Hour')[['GHI', 'DNI', 'DHI', 'Tamb']].mean()

# Plot line chart for hourly patterns
hourly_data_sierra.plot(kind='line', figsize=(10, 6), marker='o')
plt.title('Sierra Leone: Hourly Trends for GHI, DNI, DHI, and Tamb')
plt.xlabel('Hour')
plt.ylabel('Values')
plt.legend(loc='best')
plt.grid()
plt.show()

# Group data by cleaning events
cleaning_impact_sierra = sierra_df.groupby('Cleaning')[['ModA', 'ModB']].mean()

# Plot the impact of cleaning
cleaning_impact_sierra.plot(kind='bar', figsize=(8, 5), color=['blue', 'orange'])
plt.title('Sierra Leone: Impact of Cleaning on Sensor Readings (ModA and ModB)')
plt.xlabel('Cleaning Event')
plt.ylabel('Sensor Values')
plt.legend(loc='best')
plt.grid()
plt.show()



# Convert 'Timestamp' column to datetime
togo_df['Timestamp'] = pd.to_datetime(togo_df['Timestamp'])

# Extract time components
togo_df['Month'] = togo_df['Timestamp'].dt.month
togo_df['Day'] = togo_df['Timestamp'].dt.day
togo_df['Hour'] = togo_df['Timestamp'].dt.hour

# Aggregate data by month
monthly_data_togo = togo_df.groupby('Month')[['GHI', 'DNI', 'DHI', 'Tamb']].mean()

# Plot line chart for monthly trends
monthly_data_togo.plot(kind='line', figsize=(10, 6), marker='o')
plt.title('Togo: Monthly Trends for GHI, DNI, DHI, and Tamb')
plt.xlabel('Month')
plt.ylabel('Values')
plt.legend(loc='best')
plt.grid()
plt.show()


# Aggregate data by hour
hourly_data_togo = togo_df.groupby('Hour')[['GHI', 'DNI', 'DHI', 'Tamb']].mean()

# Plot line chart for hourly patterns
hourly_data_togo.plot(kind='line', figsize=(10, 6), marker='o')
plt.title('Togo: Hourly Trends for GHI, DNI, DHI, and Tamb')
plt.xlabel('Hour')
plt.ylabel('Values')
plt.legend(loc='best')
plt.grid()
plt.show()

# Group data by cleaning events
cleaning_impact_togo = togo_df.groupby('Cleaning')[['ModA', 'ModB']].mean()

# Plot the impact of cleaning
cleaning_impact_togo.plot(kind='bar', figsize=(8, 5), color=['blue', 'orange'])
plt.title('Togo: Impact of Cleaning on Sensor Readings (ModA and ModB)')
plt.xlabel('Cleaning Event')
plt.ylabel('Sensor Values')
plt.legend(loc='best')
plt.grid()
plt.show()



# Select relevant columns
correlation_cols = ['GHI', 'DNI', 'DHI', 'TModA', 'TModB']
correlation_matrix = benin_df[correlation_cols].corr()

# Plot the heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Correlation Matrix: Solar Radiation and Temperature")
plt.show()
# Plot pair plots for solar radiation and temperature measures
sns.pairplot(benin_df[correlation_cols], diag_kind="kde", corner=True)
plt.suptitle("Pair Plot: Solar Radiation and Temperature", y=1.02)
plt.show()
# Select relevant columns for wind and solar irradiance
wind_solar_cols = ['WS', 'WSgust', 'WD', 'GHI', 'DNI', 'DHI']

# Pair plot to visualize scatter relationships
sns.pairplot(benin_df[wind_solar_cols], diag_kind="kde", corner=True)
plt.suptitle("Scatter Matrix: Wind Conditions and Solar Irradiance", y=1.02)
plt.show()

# For Sierra Leone
correlation_matrix_sierra = sierra_df[correlation_cols].corr()
sns.heatmap(correlation_matrix_sierra, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Sierra Leone: Correlation Matrix")
plt.show()

# For Togo
correlation_matrix_togo = togo_df[correlation_cols].corr()
sns.heatmap(correlation_matrix_togo, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Togo: Correlation Matrix")
plt.show()


# Convert WD (wind direction) to numeric if needed
benin_df['WD'] = pd.to_numeric(benin_df['WD'], errors='coerce')

# Bin wind direction into 8 compass directions (N, NE, E, SE, S, SW, W, NW)
wind_bins = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
benin_df['Wind Bin'] = pd.cut(
    benin_df['WD'], bins=np.linspace(0, 360, 9), labels=wind_bins, include_lowest=True
)

# Calculate mean wind speed for each bin
wind_analysis = benin_df.groupby('Wind Bin', observed=False)['WS'].mean()

# Radial plot
angles = np.linspace(0, 2 * np.pi, len(wind_bins), endpoint=False).tolist()
angles += angles[:1]  # Complete the circle

wind_analysis = wind_analysis.tolist()
wind_analysis += wind_analysis[:1]  # Complete the circle

fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
ax.bar(angles, wind_analysis, width=0.4, color='blue', alpha=0.6, edgecolor='black')

# Add labels
ax.set_yticks([1, 2, 3, 4])  # Adjust to your scale
ax.set_xticks(angles[:-1])
ax.set_xticklabels(wind_bins)
ax.set_title('Radial Bar Plot of Wind Speed and Direction', va='bottom')
plt.show()


# Create a wind rose plot
fig = plt.figure(figsize=(8, 6))
ax = WindroseAxes.from_ax(fig=fig)
ax.bar(benin_df['WD'], benin_df['WS'], normed=True, opening=0.8, edgecolor='black', cmap='viridis')

# Add labels and title
ax.set_title("Wind Rose: Wind Speed and Direction")
ax.set_legend(title="Wind Speed (m/s)")
plt.show()

wind_direction_std = benin_df['WD'].std()
print("Standard Deviation of Wind Direction:", wind_direction_std)

plt.figure(figsize=(10, 6))
plt.plot(benin_df['Timestamp'], benin_df['WD'], color='blue', alpha=0.7)
plt.title("Wind Direction Variability Over Time")
plt.xlabel("Time")
plt.ylabel("Wind Direction (degrees)")
plt.grid()
plt.show()
# Create a wind rose plot
fig = plt.figure(figsize=(8, 6))
ax = WindroseAxes.from_ax(fig=fig)
ax.bar(
    benin_df['WD'], 
    benin_df['WS'], 
    normed=True, 
    opening=0.8, 
    edgecolor='black', 
    cmap=cm.get_cmap('viridis')  # Pass colormap object instead of a string
)

# Add labels and title
ax.set_title("Wind Rose: Wind Speed and Direction")
ax.set_legend(title="Wind Speed (m/s)")
plt.show()



# Scatter Plot: RH vs. Temperature and Solar Radiation
fig, axes = plt.subplots(2, 3, figsize=(18, 10))

# RH vs. TModA
sns.scatterplot(x=benin_df['RH'], y=benin_df['TModA'], ax=axes[0, 0], color='b')
axes[0, 0].set_title('RH vs. TModA')
axes[0, 0].set_xlabel('Relative Humidity (%)')
axes[0, 0].set_ylabel('Temperature (TModA)')

# RH vs. TModB
sns.scatterplot(x=benin_df['RH'], y=benin_df['TModB'], ax=axes[0, 1], color='g')
axes[0, 1].set_title('RH vs. TModB')
axes[0, 1].set_xlabel('Relative Humidity (%)')
axes[0, 1].set_ylabel('Temperature (TModB)')

# RH vs. GHI
sns.scatterplot(x=benin_df['RH'], y=benin_df['GHI'], ax=axes[0, 2], color='r')
axes[0, 2].set_title('RH vs. GHI')
axes[0, 2].set_xlabel('Relative Humidity (%)')
axes[0, 2].set_ylabel('Global Horizontal Irradiance (GHI)')

# RH vs. DNI
sns.scatterplot(x=benin_df['RH'], y=benin_df['DNI'], ax=axes[1, 0], color='c')
axes[1, 0].set_title('RH vs. DNI')
axes[1, 0].set_xlabel('Relative Humidity (%)')
axes[1, 0].set_ylabel('Direct Normal Irradiance (DNI)')

# RH vs. DHI
sns.scatterplot(x=benin_df['RH'], y=benin_df['DHI'], ax=axes[1, 1], color='m')
axes[1, 1].set_title('RH vs. DHI')
axes[1, 1].set_xlabel('Relative Humidity (%)')
axes[1, 1].set_ylabel('Diffuse Horizontal Irradiance (DHI)')

# Hide the unused plot
axes[1, 2].axis('off')

plt.tight_layout()
plt.show()

# Select columns of interest for correlation
correlation_cols = ['RH', 'TModA', 'TModB', 'GHI', 'DNI', 'DHI']
correlation_matrix = benin_df[correlation_cols].corr()

# Plot the correlation matrix
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title("Correlation Matrix: RH vs Temperature and Solar Radiation")
plt.show()


# Prepare the data for regression (RH vs Temperature)
X = benin_df[['RH']]  # Predictor (Relative Humidity)
y_tmoda = benin_df['TModA']  # Target (Temperature TModA)

# Perform linear regression
model_tmoda = LinearRegression()
model_tmoda.fit(X, y_tmoda)

# Predict and plot the regression line
y_pred_tmoda = model_tmoda.predict(X)
plt.figure(figsize=(8, 6))
plt.scatter(benin_df['RH'], benin_df['TModA'], color='b', label='Actual Data')
plt.plot(benin_df['RH'], y_pred_tmoda, color='r', label='Regression Line')
plt.title("Linear Regression: RH vs TModA")
plt.xlabel('Relative Humidity (%)')
plt.ylabel('Temperature (TModA)')
plt.legend()
plt.grid()
plt.show()


# Scatter Plot: RH vs. Temperature and Solar Radiation
fig, axes = plt.subplots(3, 3, figsize=(18, 18))

# RH vs. TModA
sns.scatterplot(x=benin_df['RH'], y=benin_df['TModA'], ax=axes[0, 0], color='b')
axes[0, 0].set_title('RH vs. TModA')
axes[0, 0].set_xlabel('Relative Humidity (%)')
axes[0, 0].set_ylabel('Temperature (TModA)')

# RH vs. TModB
sns.scatterplot(x=benin_df['RH'], y=benin_df['TModB'], ax=axes[0, 1], color='g')
axes[0, 1].set_title('RH vs. TModB')
axes[0, 1].set_xlabel('Relative Humidity (%)')
axes[0, 1].set_ylabel('Temperature (TModB)')

# RH vs. GHI
sns.scatterplot(x=benin_df['RH'], y=benin_df['GHI'], ax=axes[0, 2], color='r')
axes[0, 2].set_title('RH vs. GHI')
axes[0, 2].set_xlabel('Relative Humidity (%)')
axes[0, 2].set_ylabel('Global Horizontal Irradiance (GHI)')

# RH vs. DNI
sns.scatterplot(x=benin_df['RH'], y=benin_df['DNI'], ax=axes[1, 0], color='c')
axes[1, 0].set_title('RH vs. DNI')
axes[1, 0].set_xlabel('Relative Humidity (%)')
axes[1, 0].set_ylabel('Direct Normal Irradiance (DNI)')

# RH vs. DHI
sns.scatterplot(x=benin_df['RH'], y=benin_df['DHI'], ax=axes[1, 1], color='m')
axes[1, 1].set_title('RH vs. DHI')
axes[1, 1].set_xlabel('Relative Humidity (%)')
axes[1, 1].set_ylabel('Diffuse Horizontal Irradiance (DHI)')

# Hide the unused plot
axes[1, 2].axis('off')

plt.tight_layout()
plt.show()

# Select columns of interest for correlation
correlation_cols = ['RH', 'TModA', 'TModB', 'GHI', 'DNI', 'DHI']
correlation_matrix = benin_df[correlation_cols].corr()

# Plot the correlation matrix
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title("Correlation Matrix: RH vs Temperature and Solar Radiation")
plt.show()


from sklearn.linear_model import LinearRegression

# Prepare the data for regression (RH vs Temperature)
X = benin_df[['RH']]  # Predictor (Relative Humidity)
y_tmoda = benin_df['TModA']  # Target (Temperature TModA)

# Perform linear regression
model_tmoda = LinearRegression()
model_tmoda.fit(X, y_tmoda)

# Predict and plot the regression line for TModA
y_pred_tmoda = model_tmoda.predict(X)
plt.figure(figsize=(8, 6))
plt.scatter(benin_df['RH'], benin_df['TModA'], color='b', label='Actual Data')
plt.plot(benin_df['RH'], y_pred_tmoda, color='r', label='Regression Line')
plt.title("Linear Regression: RH vs TModA")
plt.xlabel('Relative Humidity (%)')
plt.ylabel('Temperature (TModA)')
plt.legend()
plt.grid()
plt.show()

y_tmodb = benin_df['TModB']  # Target (Temperature TModB)
model_tmodb = LinearRegression()
model_tmodb.fit(X, y_tmodb)

# Predict and plot the regression line for TModB
y_pred_tmodb = model_tmodb.predict(X)
plt.figure(figsize=(8, 6))
plt.scatter(benin_df['RH'], benin_df['TModB'], color='g', label='Actual Data')
plt.plot(benin_df['RH'], y_pred_tmodb, color='r', label='Regression Line')
plt.title("Linear Regression: RH vs TModB")
plt.xlabel('Relative Humidity (%)')
plt.ylabel('Temperature (TModB)')
plt.legend()
plt.grid()
plt.show()

y_ghi = benin_df['GHI']  # Target (Global Horizontal Irradiance GHI)
model_ghi = LinearRegression()
model_ghi.fit(X, y_ghi)

# Predict and plot the regression line for GHI
y_pred_ghi = model_ghi.predict(X)
plt.figure(figsize=(8, 6))
plt.scatter(benin_df['RH'], benin_df['GHI'], color='r', label='Actual Data')
plt.plot(benin_df['RH'], y_pred_ghi, color='y', label='Regression Line')
plt.title("Linear Regression: RH vs GHI")
plt.xlabel('Relative Humidity (%)')
plt.ylabel('Global Horizontal Irradiance (GHI)')
plt.legend()
plt.grid()
plt.show()

y_dni = benin_df['DNI']  # Target (Direct Normal Irradiance DNI)
model_dni = LinearRegression()
model_dni.fit(X, y_dni)

# Predict and plot the regression line for DNI
y_pred_dni = model_dni.predict(X)
plt.figure(figsize=(8, 6))
plt.scatter(benin_df['RH'], benin_df['DNI'], color='c', label='Actual Data')
plt.plot(benin_df['RH'], y_pred_dni, color='y', label='Regression Line')
plt.title("Linear Regression: RH vs DNI")
plt.xlabel('Relative Humidity (%)')
plt.ylabel('Direct Normal Irradiance (DNI)')
plt.legend()
plt.grid()
plt.show()

y_dhi = benin_df['DHI']  # Target (Diffuse Horizontal Irradiance DHI)
model_dhi = LinearRegression()
model_dhi.fit(X, y_dhi)

# Predict and plot the regression line for DHI
y_pred_dhi = model_dhi.predict(X)
plt.figure(figsize=(8, 6))
plt.scatter(benin_df['RH'], benin_df['DHI'], color='m', label='Actual Data')
plt.plot(benin_df['RH'], y_pred_dhi, color='r', label='Regression Line')
plt.title("Linear Regression: RH vs DHI")
plt.xlabel('Relative Humidity (%)')
plt.ylabel('Diffuse Horizontal Irradiance (DHI)')
plt.legend()
plt.grid()
plt.show()


# histograms

# List of variables for which we want to plot histograms
variables = ['GHI', 'DNI', 'DHI', 'WS', 'TModA', 'TModB']

# Set up the subplots: 2 rows and 3 columns for the 6 variables
fig, axes = plt.subplots(2, 3, figsize=(18, 10))

# Plot histograms for each variable
for i, var in enumerate(variables):
    ax = axes[i // 3, i % 3]  # Determine position in the subplot grid
    sns.histplot(benin_df[var], kde=True, bins=30, color='blue', ax=ax)  # kde=True adds the density curve
    ax.set_title(f'Histogram of {var}')
    ax.set_xlabel(var)
    ax.set_ylabel('Frequency')
    ax.grid(True)

# Adjust the layout to make room for titles
plt.tight_layout()
plt.show()
z- score analysis



# List of variables for which we will calculate the Z-scores
variables = ['GHI', 'DNI', 'DHI', 'WS', 'TModA', 'TModB']

# Calculate Z-scores for each variable
z_scores = benin_df[variables].apply(zscore)

# Show the Z-scores for the first few rows
print("Z-Scores for each variable:\n", z_scores.head())

# Flag the data points that are outliers (Z-score > 3 or Z-score < -3)
outliers = (z_scores.abs() > 3)

# Display the outliers (True means outlier)
print("\nOutliers Flagged (True = Outlier, False = Normal):\n", outliers)

# For each variable, show how many outliers exist
outlier_count = outliers.sum()
print("\nOutliers Count per Variable:\n", outlier_count)

# Optionally, visualize the Z-scores using histograms
fig, axes = plt.subplots(2, 3, figsize=(18, 10))

for i, var in enumerate(variables):
    ax = axes[i // 3, i % 3]
    sns.histplot(z_scores[var], kde=True, bins=30, color='purple', ax=ax)
    ax.set_title(f'Z-Scores Distribution for {var}')
    ax.set_xlabel('Z-Score')
    ax.set_ylabel('Frequency')
    ax.grid(True)

plt.tight_layout()
plt.show()



# Variables to use for the bubble chart
x = benin_df['GHI']  # X-axis: GHI
y = benin_df['TEMP']  # Y-axis: Temperature (Tamb)
size = benin_df['RH']  # Bubble size: Relative Humidity (RH) or BP (Barometric Pressure)

# Normalize the bubble size for better visualization
# We can normalize by scaling the size of the bubbles
size = (size - size.min()) / (size.max() - size.min()) * 1000  # Normalize to range 0-1000

# Create the bubble chart
plt.figure(figsize=(10, 6))
scatter = plt.scatter(x, y, s=size, c=size, cmap='viridis', alpha=0.6, edgecolors="w", linewidth=0.5)

# Add labels and title
plt.title('Bubble Chart: GHI vs. Tamb vs. RH')
plt.xlabel('Global Horizontal Irradiance (GHI)')
plt.ylabel('Temperature (Tamb)')
plt.colorbar(scatter, label='Relative Humidity (RH)')  # Color bar to indicate the RH values

plt.grid(True)
plt.show()
