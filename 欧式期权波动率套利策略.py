import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import akshare as ak
from scipy.optimize import brentq
from scipy.stats import norm




# 获取上证50ETF的历史价格数据
stock_data = yf.download("510050.SS", start="2021-01-01", end="2022-01-01")

# 提取调整后的收盘价数据
adj_close_prices = stock_data['Adj Close']

# 绘制折线图
plt.figure(figsize=(10, 6))
adj_close_prices.plot(color='blue')
plt.title('SSE 50ETF (510050) price history', fontsize=16)
plt.xlabel('date', fontsize=14)
plt.ylabel('price', fontsize=14)
plt.grid(True)
plt.show()



# 计算收益率
returns = stock_data['Adj Close'].pct_change().dropna()

# 计算历史波动率
historical_volatility = np.std(returns) * np.sqrt(252)

print("上证50ETF的历史波动率为：", historical_volatility)


#获取上证50ETF期权矩阵数据
option_finance_board_df = ak.option_finance_board(symbol="华夏上证50ETF期权", end_month="2406")
print(option_finance_board_df)


# 筛选出指定合约交易代码的数据
contract_code = "510050P2406M02500"  # 你想要筛选的合约交易代码
filtered_data = option_finance_board_df[option_finance_board_df['合约交易代码'] == contract_code]

# 提取当前价、行权价和日期
current_price = filtered_data['当前价'].values[0]
strike_price = filtered_data['行权价'].values[0]
date = filtered_data['日期'].values[0]

print("日期:", date)
print("当前价:", current_price)
print("行权价:", strike_price)

# 实现布莱克-斯克尔斯看涨期权定价公式
def black_scholes_call(S, K, r, q, T, sigma):
    # 计算d1和d2参数
    d1 = (np.log(S / K) + (r - q + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    # 根据d1和d2计算看涨期权的理论价格
    call_price = (S * np.exp(-q * T) * norm.cdf(d1)) - (K * np.exp(-r * T) * norm.cdf(d2))
    return call_price

# 实现布莱克-斯克尔斯看跌期权定价公式
def black_scholes_put(S, K, r, q, T, sigma):
    # 计算d1和d2参数
    d1 = (np.log(S / K) + (r - q + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    # 根据d1和d2计算看跌期权的理论价格
    put_price = (K * np.exp(-r * T) * norm.cdf(-d2)) - (S * np.exp(-q * T) * norm.cdf(-d1))
    return put_price


# 实现计算隐含波动率的函数
def implied_volatility(C_market, S, K, r, q, T, option_type='call'):
    # 定义目标函数：市场价格与理论价格的差异
    def objective(sigma):
        if option_type == 'call':
            return black_scholes_call(S, K, r, q, T, sigma) - C_market
        else:
            return black_scholes_put(S, K, r, q, T, sigma) - C_market

    # 使用brentq方法求解使目标函数为零的波动率
    return brentq(objective, 0.0001, 2.0)


def execute_volatility_arbitrage(historical_volatility,implied_vol):
    if historical_volatility > implied_vol:
        print("标的历史波动率大于该期权的隐含波动率，应该买入")
    elif historical_volatility < implied_vol:
        print("标的历史波动率小于该期权的隐含波动率，应该卖出")


# 设置示例参数
C_market = current_price  # 已知的看涨/跌期权市场价格
S = 2.525  # 标的资产当前价格（上证50 ETF）
K = strike_price    # 行权价格
r = 0.03 # 年化无风险利率（以小数形式）
q = 0.01621 # 年化股息率（以小数形式）
T = 0.126   # 期权到期时间（以年为单位）
option_type='put'


# 计算隐含波动率
implied_vol = implied_volatility(C_market, S, K, r, q, T,option_type)
if option_type == 'put':
    print("看跌期权的隐含波动率:",implied_vol)
else:
    print("看涨期权的隐含波动率:",implied_vol)

execute_volatility_arbitrage(historical_volatility,implied_vol)



