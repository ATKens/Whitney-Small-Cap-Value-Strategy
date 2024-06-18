import pandas as pd
import akshare as ak


symbol_path = 'NASDAQ_Symbols.csv'
path = 'NASDAQ_Stock_List.csv'



"""
获取NSDAQ汇总数据中符合条件的矩阵
"""
def get_symbol_column_from_csv(file_path):
    # 读取CSV文件
    data_frame = pd.read_csv(file_path, encoding='utf-8-sig')

    # 检查 "symbol" 列是否在DataFrame中
    if 'symbol' in data_frame.columns:
        return data_frame['symbol']
    else:
        raise ValueError("CSV文件中不存在 'symbol' 列")






# 获取美国纳斯达克股票列表
stock_us_nasdaq_df = ak.stock_us_spot()

# nsdaq总汇总(包括各种信息的数据矩阵)保存到 CSV 文件，指定使用 UTF-8 编码
stock_us_nasdaq_df.to_csv(path, encoding='utf-8-sig')


# 筛选出symbol数据矩阵
symbols = get_symbol_column_from_csv(path)


# 保存symbol数据矩阵
symbols.to_csv(symbol_path, encoding='utf-8-sig')



# 读取大 DataFrame
df = pd.read_csv(symbol_path)

# 确定每个小 DataFrame 的大小
num_splits = 80
split_size = len(df) // num_splits + (len(df) % num_splits > 0)

# 分割并保存
for i in range(num_splits):
    start_index = i * split_size
    end_index = start_index + split_size
    small_df = df.iloc[start_index:end_index]

    # 保存为 .csv 文件
    small_df.to_csv(f'small_dataframe_part_{i + 1}.csv', index=False, encoding='utf-8-sig')

print("DataFrames have been split and saved.")



