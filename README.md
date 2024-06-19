# Whitney Small Cap Value Strategy
# 惠特尼小型价值股投资策略

## Overview
## 概览

The Whitney Small Cap Value Strategy is an investment approach developed by Whitney George, renowned for his expertise in small cap stocks. Recognized as the "Best Fund Manager" by Financial Intelligence Monthly in January 2011, George's strategy focuses on identifying undervalued small cap stocks that offer substantial growth potential.

惠特尼小型价值股投资策略是由著名小型股投资专家惠特尼·乔治开发的一种投资方法。乔治因其在小型股投资领域的专长于2011年1月被《财智月刊》评为“最佳基金经理”。该策略专注于识别具有巨大增长潜力的低估小型股。

## Investment Philosophy
## 投资哲学

The strategy is built on the premise that small cap stocks, often overlooked by large investors, can provide superior returns. George's approach is meticulous, focusing on stocks that meet the following criteria:

该策略基于这样一个前提：小型股常常被大投资者忽视，但它们能提供超额回报。乔治的方法非常细致，专注于符合以下标准的股票：

- **Market Capitalization:** Below the average market cap across the market.
- **市值:** 低于市场平均市值。

- **Debt-to-Equity Ratio:** Lower than the market average, indicating solid financial health.
- **负债与权益比:** 低于市场平均水平，表明财务状况良好。

- **Free Cash Flow Per Share:** Higher than the market average, suggesting efficient operation and profitability.
- **每股自由现金流:** 高于市场平均水平，表明运营效率高和盈利能力强。

- **Return on Assets and Equity:** Higher than average, indicating effective management and profitable asset use.
- **资产和权益回报率:** 高于平均水平，表明管理有效且资产使用盈利。

- **Price-to-Earnings Ratio:** Below the market average, pointing to undervalued stocks.
- **市盈率:** 低于市场平均水平，指向被低估的股票。

- **Price-to-Book and Price-to-Sales Ratios:** Lower than the market average, further indicating undervaluation.
- **市净率和市销率:** 低于市场平均水平，进一步表明股票被低估。

## How It Works
## 工作原理

This strategy uses quantitative metrics to screen small cap stocks across various industries, excluding sectors like banking, non-bank financials, steel, mining, food & beverages, and communications due to historical underperformance.

该策略使用定量指标筛选各行业的小型股，由于历史表现不佳，排除了银行、非银行金融、钢铁、采矿、食品饮料和通信等行业。

## Usage
## 使用方法
**步骤1**运行StrategyIni.py 进行初始化
执行步骤1后得到
NASDAQ_Stock_List.csv  NASDAQ_Symbols.csv  small_dataframe_part_1~80.csv

**步骤2**运行FilterModule.py 过滤模块
执行步骤2后得到
financial_data_all.csv  financial_data_1~80.csv  filtered_stocks.json
其中filtered_stocks.json是最终筛选的数据

**注意**:是否同时运行两个步骤取决于你的调整周期,假设周期为1day,那么StrategyIni.py只运行一次,
如果周期为半年以上,那么在筛选时需要执行步骤1和步骤2

## Contributions
## 贡献

Contributions to this strategy are welcome. Please ensure any pull requests or issues adhere to the existing criteria for stock selection and valuation.

欢迎对这一策略做出贡献。请确保所有的拉取请求或问题都符合现有的股票选择和估值标准。

## License
## 许可证

This strategy is distributed under the MIT License. See `LICENSE` for more information.

该策略在MIT许可证下发布。有关更多信息，请查看`LICENSE`文件。

## Contact
## 联系方式

For more information, please contact [traderAJ](#) profile.

如需更多信息，请联系 [traderAJ](#) 个人资料。

Happy Investing!
祝投资愉快！
