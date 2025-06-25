
# Trader Behavior Insights Assignment

## 📊 Objective
This project explores the relationship between crypto trader performance and Bitcoin market sentiment. Using historical trading data and the Bitcoin Fear & Greed Index, we aim to extract insights into how trader behavior varies under different market conditions.

---

## 📁 Datasets Used

### 1. `historical_data.csv`
- Source: Hyperliquid trading platform
- Key Columns:
  - `Timestamp IST`: Execution timestamp
  - `Closed PnL`: Profit and loss on the trade
  - `Size USD`: Trade size in USD
  - `Side`: Buy/Sell
  - `Account`, `Execution Price`, `Coin`, etc.

### 2. `fear_greed_index.csv`
- Source: Bitcoin Fear & Greed Index
- Key Columns:
  - `date`: Date in YYYY-MM-DD format
  - `classification`: Market sentiment (e.g., Fear, Greed, Extreme Fear)

---

## 🛠️ Tasks Performed

1. **Data Loading and Cleaning**
   - Parsed timestamps and dates into consistent formats
   - Merged sentiment data with trading data on `date`

2. **Feature Engineering**
   - `win_trade`: True if `Closed PnL > 0`
   - `loss_trade`: True if `Closed PnL < 0`
   - `PnL_per_USD`: `Closed PnL / Size USD` (with divide-by-zero protection)

3. **Analysis**
   - Grouped by `classification` to calculate:
     - Average Closed PnL
     - Win Rate
     - Average Trade Size (USD)

4. **Visualizations**
   - 📦 Boxplot of Closed PnL by market sentiment
   - 📊 Bar chart of Win Rate by market sentiment

---

## 📈 Visual Output

- `closed_pnl_boxplot.png`: Shows distribution of Closed PnL by sentiment
- `win_rate_barplot.png`: Shows win rate per sentiment classification

---

## ▶️ How to Run

1. Make sure you have Python 3 installed
2. Install required libraries:
```bash
pip install pandas matplotlib seaborn
```
3. Run the script:
```bash
python trader_behavior_insights.py
```

---

## 🧠 Key Insight

Trader profitability and win rate are influenced by market sentiment. This kind of sentiment-performance analysis can inform smarter trading strategies by adapting to behavioral patterns across Fear and Greed cycles.

---
