import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_excel("weatherdata1.xlsx")

# Display the first few rows
print("Data Preview:")
print(df.head())


print("\nSummary Statistics:")
print(df.describe())


sns.set(style="whitegrid")


plt.figure(figsize=(10, 5))
sns.lineplot(data=df, x="Year", y="Avg_Temperature", marker='o', color='red')
plt.title("Yearly Average Temperature (2000–2025)")
plt.ylabel("Temperature (°C)")
plt.xlabel("Year")
plt.grid(True)
plt.tight_layout()
plt.show()


plt.figure(figsize=(10, 5))
sns.barplot(data=df, x="Year", y="Avg_Humidity", color='skyblue')
plt.title("Yearly Average Humidity (2000–2025)")
plt.ylabel("Humidity (%)")
plt.xlabel("Year")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


plt.figure(figsize=(10, 5))
sns.lineplot(data=df, x="Year", y="Total_Rainfall", marker='o', color='green')
plt.title("Total Yearly Rainfall (2000–2025)")
plt.ylabel("Rainfall (mm)")
plt.xlabel("Year")
plt.grid(True)
plt.tight_layout()
plt.show()



hottest_year = df[df['Avg_Temperature'] == df['Avg_Temperature'].max()]
coldest_year = df[df['Avg_Temperature'] == df['Avg_Temperature'].min()]

print("\nHottest Year:")
print(hottest_year)

print("\nColdest Year:")
print(coldest_year)


print("\nOverall Averages:")
print("Average Temperature:", round(df['Avg_Temperature'].mean(), 2), "°C")
print("Average Humidity:", round(df['Avg_Humidity'].mean(), 2), "%")
print("Average Yearly Rainfall:", round(df['Total_Rainfall'].mean(), 2), "mm")
