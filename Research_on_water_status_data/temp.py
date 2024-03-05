import pandas as pd

# 读取csv文件
df = pd.read_csv('airside_waterflow_210A.csv')

# 根据第一列和第二列排序
df_sorted = df.sort_values(by=['ratio', 'temperature'])

# 打印排序后的DataFrame
print(df_sorted)

df_sorted.to_csv("output.csv",index=False)