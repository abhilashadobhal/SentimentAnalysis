# DataScienceProject
## Summary & Strategy Recommendations

# Bitcoin Sentiment Analysis Project

## Project Goal
Analyze how market sentiment (Fear/Greed) relates to trader behavior and performance on Hyperliquid to uncover patterns for smarter trading.

## Structure
- `DataScienceProject.ipynb`: The main data processing and analysis notebook.
- `README.md`: Key insights and strategic recommendations.
- `fear_greed_index.csv`: Historical Fear/Greed sentiment data.
- `historical_data.csv`: Trader performance data from Hyperliquid.

## Key Findings
- Market sentiment significantly impacts trader performance, with Fear periods showing the highest average PnL ($209K) but also the highest volatility.
- Traders adjust behavior based on sentiment, increasing trade frequency and long positions during Greed.
- Segmentation reveals patterns: high-risk traders underperform in Fear, frequent traders profit more in Greed, and consistent traders maintain stability.

## Analysis Results Overview

### Performance by Sentiment
- **Fear**: Highest average PnL ($209K), median PnL ($81K), win rate 41.6%, volatility $380K, 133K total trades.
- **Greed**: Average PnL $99K, median $36K, win rate 37.4%, volatility $283K, 36K trades.
- **Extreme Greed**: Average PnL $35K, median $0, win rate 33.7%, volatility $85K, 7K trades.
- **Neutral**: Average PnL $20K, median -$0.4, win rate 26.1%, volatility $57K, 7K trades.

### Behavioral Changes by Sentiment
- **Fear**: Avg trades/day 4,183, avg trade size $5,927, long ratio 45.9%.
- **Neutral**: Avg trades/day 893, avg trade size $3,793, long ratio 46.9%.
- **Greed**: Avg trades/day 1,134, avg trade size $5,839, long ratio 49.6%.
- **Extreme Greed**: Avg trades/day 1,392, avg trade size $4,344, long ratio 51.8%.

### Segmentation Insights
- **Risk Impact in Fear**: High-risk/size traders have lower win rates (40.5% vs 43.0%) and higher volatility ($480K vs $162K) compared to low-risk traders.
- **Frequency in Greed**: Frequent traders show higher median PnL ($69K vs $16K) and win rates (45.4% vs 34.3%) than infrequent traders.
- **Consistency Across Sentiments**: Consistent traders maintain stable PnL, while inconsistent traders experience higher volatility, especially in Fear and Greed.

## Strategy Recommendations

### Rule 1: Sentiment-Based Position Sizing
Reduce trade sizes during Fear periods due to high volatility. Consider halving positions or sitting out during Neutral sentiment where win rates are lowest (26.1%).

### Rule 2: Leverage and Risk Management
Cap trade sizes during Fear to avoid the leverage trap. High-risk traders underperform significantly in fearful markets.

### Rule 3: Frequency Optimization
Increase trading frequency during Greed periods, as frequent traders outperform infrequent ones in bullish sentiment.

### Rule 4: Focus on Consistency
Prioritize strategies that promote consistent performance over chasing high-volatility opportunities, as consistent traders show stable results across all sentiments.


