import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
hour = pd.read_csv('hour.csv')

# Scatter plot for bike ridership count by hour
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(x=hour['instant'], y=hour['count'])
plt.xlabel("Hour")
plt.ylabel("Count")
plt.title("Ridership Count by Hour")
plt.show()

# Boxplot for registered bike users by hour
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(x='hr', y='registered', data=hour)
plt.xlabel("Hour")
plt.ylabel("Count")
plt.title("Count by Hour")
plt.show()

# Heatmap of bike ridership count by hour and weekday
df_hm = hour.pivot_table(index='hr', columns='weekday', values='count')
plt.figure(figsize=(20, 10))
sns.heatmap(df_hm, fmt="d", cmap='binary', linewidths=.5, vmin=0)
plt.title("Heatmap of Ridership Count")
plt.show()