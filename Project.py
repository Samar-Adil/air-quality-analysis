# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from statsmodels.stats.weightstats import ztest

# LOAD DATA
df = pd.read_csv('C:/Users/samar/Downloads/AirQualityDataset.csv')

# CLEAN COLUMN NAMES
df.columns = df.columns.str.strip().str.lower()


# BOXPLOT (OUTLIER ANALYSIS)


plt.figure(figsize=(8,5))
sns.boxplot(x=df["pollutant_avg"])

plt.title("Outlier Detection using Boxplot")
plt.show()


# STATE-WISE AVG POLLUTION
state_avg = df.groupby("state")["pollutant_avg"].mean().reset_index()
state_avg = state_avg.sort_values(by="pollutant_avg", ascending=False)

# BAR CHART (STATES)
plt.figure(figsize=(14,6))
sns.barplot(x="state", y="pollutant_avg", data=state_avg, color="teal")

plt.xticks(rotation=90)
plt.xlabel("States")
plt.ylabel("Average Pollution")
plt.title("State-wise Average Pollution")
plt.show()

# HISTOGRAM (DISTRIBUTION)
plt.figure(figsize=(8,5))
plt.hist(df["pollutant_avg"], bins=20, color="purple", edgecolor="black")

plt.xlabel("Pollution Avg")
plt.ylabel("Frequency")
plt.title("Distribution of Pollution")
plt.show()

# SCATTER (MAX vs AVG)
plt.figure(figsize=(8,5))
plt.scatter(df["pollutant_max"], df["pollutant_avg"], color="red")

plt.xlabel("Pollutant Max")
plt.ylabel("Pollutant Avg")
plt.title("Max vs Avg Pollution")
plt.show()


# BIHAR CITY ANALYSIS
df["state"] = df["state"].str.strip().str.lower()

bihar_df = df[df["state"] == "bihar"]

print("Total Bihar rows:", len(bihar_df))

if len(bihar_df) == 0:
    print("No Bihar data found")

city_avg = bihar_df.groupby("city")["pollutant_avg"].mean().reset_index()
city_avg = city_avg.sort_values(by="pollutant_avg", ascending=False)

plt.figure(figsize=(12,5))
plt.plot(city_avg["city"], city_avg["pollutant_avg"], marker='o')

plt.xticks(rotation=90)
plt.xlabel("City")
plt.ylabel("Pollution Avg")
plt.title("City-wise Pollution in Bihar")

plt.show()

# HEATMAP
corr_data = df[['pollutant_min', 'pollutant_max', 'pollutant_avg',
                'latitude', 'longitude']].corr()

plt.figure(figsize=(6,4))
sns.heatmap(corr_data, annot=True, fmt='.2f', cmap='coolwarm',
            linewidths=0.5, annot_kws={'size': 9})

plt.title("Heatmap: Correlation Matrix")
plt.show()

#  HYPOTHESIS TEST (Z-TEST)

print("\nHypothesis Testing:")

print("H0: Mean of pollutant_max = Mean of pollutant_avg")
print("H1: Mean of pollutant_max ≠ Mean of pollutant_avg")

z_stat, p_val = ztest(df["pollutant_max"], df["pollutant_avg"])

print("Z-Statistic:", z_stat)
print("P-Value:", p_val)

if p_val < 0.05:
    print("Conclusion: Reject H0 → Significant difference")
else:
    print("Conclusion: Accept H0 → No significant difference")
