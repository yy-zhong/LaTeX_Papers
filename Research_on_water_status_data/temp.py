import pandas as pd

# 读取csv文件
df = pd.read_csv('hydrogenside_waterflow_300A_in_ratio.csv')

# 根据第一列和第二列排序
df_sorted = df.sort_values(by=['temperature','ratio'])

# 打印排序后的DataFrame
print(df_sorted)

df_sorted = df_sorted[['temperature','ratio','waterflow']]

df_sorted.to_csv("output.csv",index=False)