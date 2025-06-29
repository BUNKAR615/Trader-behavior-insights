Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14B_POzkSGOu57ItREa7L7oD1VRPPyF0R
"""

import pandas as pd

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load datasets
historical_df = pd.read_csv("historical_data.csv")
sentiment_df = pd.read_csv("fear_greed_index.csv")

import pandas as pd

# Load both datasets
historical_df = pd.read_csv("historical_data.csv")
sentiment_df = pd.read_csv("fear_greed_index.csv")

# Display first few rows of each dataset
print("Historical Data Columns:\n", historical_df.columns)
print("\nSentiment Data Columns:\n", sentiment_df.columns)

print("\nSample Historical Data:")
print(historical_df.head())

print("\nSample Sentiment Data:")
print(sentiment_df.head())

# 2. Convert 'Timestamp IST' in historical data to date
historical_df['date'] = pd.to_datetime(historical_df['Timestamp IST'], format="%d-%m-%Y %H:%M").dt.date

# 3. Convert 'date' in sentiment data to date type
sentiment_df['date'] = pd.to_datetime(sentiment_df['date']).dt.date

# 4. Merge on 'date'
merged_df = pd.merge(historical_df, sentiment_df[['date', 'classification']], on='date', how='inner')

# 5. Create new columns
merged_df['win_trade'] = merged_df['Closed PnL'] > 0
merged_df['loss_trade'] = merged_df['Closed PnL'] < 0
merged_df['PnL_per_USD'] = merged_df['Closed PnL'] / merged_df['Size USD'].replace(0, pd.NA)

# 6. Group by classification to calculate summary statistics
grouped_stats = merged_df.groupby('classification').agg(
    average_closed_pnl=('Closed PnL', 'mean'),
    win_rate=('win_trade', 'mean'),
    average_size_usd=('Size USD', 'mean')
).reset_index()

# Print results
print("\nGrouped Summary Statistics:")
print(grouped_stats)

# 7a. Boxplot: Closed PnL by Classification
plt.figure(figsize=(10, 6))
sns.boxplot(x='classification', y='Closed PnL', data=merged_df, palette='Set2')
plt.title('Closed PnL Distribution by Market Sentiment')
plt.xlabel('Market Sentiment Classification')
plt.ylabel('Closed PnL')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 7b. Barplot: Win Rate by Classification
plt.figure(figsize=(10, 6))
sns.barplot(x='classification', y='win_rate', data=grouped_stats, palette='Set3')
plt.title('Win Rate by Market Sentiment')
plt.xlabel('Market Sentiment Classification')
plt.ylabel('Win Rate')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
