import csv
import os
from pathlib import Path

# 目标文件夹路径
target_directory = r"C:\Users\e0449219\AppData\Local\新建文件夹"

# 确保目标文件夹存在
if not os.path.exists(target_directory):
    os.makedirs(target_directory)
with open(Path(target_directory, 'random_data.csv'),mode="w+") as f:
    c=csv.DictWriter(f,fieldnames=[ f'column_{i}' for i in range(5)])
    c.writeheader()
    for i in range(1024*87040): 
        c.writerow({
            f'column_{i}': 2 for i in range(5)
        })
# # CSV文件路径
# csv_file_path = os.path.join(target_directory, 'random_data.csv')

# # 定义每行数据的平均大小（以字节为单位）
# average_row_size = 200

# # 计算所需的行数
# desired_file_size_bytes = 1 * 1024**3  # 1GB
# estimated_rows = desired_file_size_bytes // average_row_size

# # 定义列数
# num_columns = 5

# # 生成数据
# data = {
#     f'column_{i}': np.random.randint(0, 1000, size=estimated_rows) for i in range(num_columns)
# }

# # 创建DataFrame
# df = pd.DataFrame(data)

# # 将DataFrame写入CSV文件
# df.to_csv(csv_file_path, index=False)
