import yfinance as yf
import pandas as pd
from concurrent.futures import ThreadPoolExecutor, as_completed
import os
import json

path = 'NASDAQ_Stock_List.csv'


"""
获取每个stock symbol对应的数据矩阵
"""
def fetch_info(ticker, start, end):
    try:
        ticker_data = yf.Ticker(ticker)
        info = ticker_data.info

        # 获取指定日期范围的历史财务数据
        hist_data = ticker_data.history(start=start, end=end)
        #time.sleep(5)
        return {
            'Symbol': ticker,
            'Market Cap': info.get('marketCap'),
            'PE': info.get('trailingPE'),
            'PB': info.get('priceToBook'),
            'Debt to Equity': info.get('debtToEquity'),
            'Free Cash Flow Per Share': info.get('freeCashflow', 0) / info.get('sharesOutstanding', 1) if info.get(
                'freeCashflow') and info.get('sharesOutstanding') else None,
            'Total Asset Return': info.get('returnOnAssets'),
            'Capital Return': info.get('returnOnEquity'),
            'PS': info.get('priceToSalesTrailing12Months'),
            'Historical Data': hist_data['Close'].mean()
        }
    except Exception as e:
        print(f"Error processing {ticker}: {e}")
        return None

"""
线程池启动函数
"""
def get_data_concurrently(tickers, start, end):
    num_workers = len(tickers)  # 根据系统能力调整工作线程数
    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        futures = [executor.submit(fetch_info, ticker, start, end) for ticker in tickers]
        results = [future.result() for future in as_completed(futures)]

    # 过滤掉结果中的 None 对象
    valid_results = [result for result in results if result is not None]

    financials_data = pd.DataFrame(valid_results)
    # 删除包含空值的行
    financials_data.dropna(inplace=True)
    return financials_data


def load_data(file_path):
    return pd.read_csv(file_path)


def filter_stocks(df):
    filtered_stocks = []
    # 获取市场的平均值，用于比较
    market_caps_mean = df['Market Cap'].mean()
    debt_to_equity_mean = df['Debt to Equity'].mean()
    free_cash_flow_mean = df['Free Cash Flow Per Share'].mean()
    total_asset_return_mean = df['Total Asset Return'].mean()
    capital_return_mean = df['Capital Return'].mean()
    pe_mean = df['PE'].mean()
    pb_mean = df['PB'].mean()
    ps_mean = df['PS'].mean()

    # 遍历DataFrame中的每一行
    for index, row in df.iterrows():
        try:
            # 检查股票是否符合惠特尼·乔治的选股条件
            if (row['Market Cap'] < market_caps_mean and
                    row['Debt to Equity'] < debt_to_equity_mean and
                    row['Free Cash Flow Per Share'] > free_cash_flow_mean and
                    row['Total Asset Return'] > total_asset_return_mean and
                    row['Capital Return'] > capital_return_mean and
                    row['PE'] < pe_mean and
                    row['PB'] < pb_mean and
                    row['PS'] < ps_mean):
                filtered_stocks.append(row['Symbol'])
        except Exception as e:
            print(f"Error processing {row['Symbol']}: {e}")
    return filtered_stocks



def save_to_json(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f)





""""""
# 定义日期范围
start_date = '2024-01-01'
end_date = '2024-05-01'

# 循环遍历每个小的 DataFrame 文件
for i in range(1, 81):  # 从1到80
    # 构建文件名
    file_name = f'small_dataframe_part_{i}.csv'

    # 读取 DataFrame
    data_frame = pd.read_csv(file_name, encoding='utf-8-sig')

    # 提取 'symbol' 列并转换为列表，排除任何空值
    tickers = data_frame['symbol'].dropna().tolist()

    # 获取指定日期范围内的财务数据
    financial_data = get_data_concurrently(tickers, start_date, end_date)

    # 保存财务数据到 CSV 文件
    output_file_name = f'financial_data{i}.csv'
    financial_data.to_csv(output_file_name, encoding='utf-8-sig')

print("所有financial_data文件处理完成。")



# 创建一个空的DataFrame来存储所有数据
combined_df = pd.DataFrame()

# 循环遍历每个文件并合并
for i in range(1, 81):  # 从1到80
    file_name = f'financial_data{i}.csv'
    if os.path.exists(file_name):  # 检查文件是否存在
        # 读取每个文件
        df = pd.read_csv(file_name, encoding='utf-8-sig')
        # 将其添加到combined_df中
        combined_df = pd.concat([combined_df, df], ignore_index=True)

# 保存合并后的DataFrame到新的CSV文件
combined_df.to_csv('financial_data_all.csv', index=False, encoding='utf-8-sig')

print("All financial data has been merged into financial_data_all.csv.")





# 加载数据
data_frame = load_data('financial_data_all.csv')
filtered_tickers = filter_stocks(data_frame)
# 调用函数，保存到文件
save_to_json('filtered_stocks.json', filtered_tickers)
print("Filtered stocks have been saved to 'filtered_stocks.json'")
