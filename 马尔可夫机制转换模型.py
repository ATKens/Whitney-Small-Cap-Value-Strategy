"""
模型目标
估计每个状态的特性：

找出每个状态的平均股价水平（通过截距）和波动性（通过方差）。
了解状态之间如何转换：

模型将估计从牛市转向熊市的概率，以及从熊市转向牛市的概率。
状态概率：

模型可以告诉我们在任何特定时间点，市场处于牛市或熊市的概率

核心函数：MarkovRegression
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.tsa.regime_switching.markov_regression import MarkovRegression

# 示例数据加载，这里使用模拟数据，请用实际股市数据替换
np.random.seed(1)
n_samples = 1000
sigma = 0.1
shocks = sigma * np.random.normal(size=n_samples)
regimes = np.random.choice([0, 1], size=n_samples, p=[0.8, 0.2])
y = 0.2 * regimes - 0.1 * (1 - regimes) + shocks

# 创建一个时间序列索引
index = pd.date_range("2000-01-01", periods=n_samples, freq="D")
data = pd.Series(y, index=index)#data就是构建好的时间序列

# 使用MarkovRegression模型
model = MarkovRegression(data, k_regimes=2, trend='c', switching_variance=True)
print("model:",model)

results = model.fit()


# 打印模型结果
print(results.summary())

# 绘制状态
fig, ax = plt.subplots()
ax.plot(results.smoothed_marginal_probabilities[0], label="Prob of Bear Market")
ax.plot(results.smoothed_marginal_probabilities[1], label="Prob of Bull Market")
ax.set(title='Markov Switching Model - Probability of Market Regimes')
ax.legend()
plt.show()
