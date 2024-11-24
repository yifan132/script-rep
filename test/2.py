import os
import csv

# 指定文件夹路径
folder_path = 'C:\\Users\\e0449219\\Downloads\\1'

# 指定合并后的文件名和路径
output_file_path = os.path.join(folder_path, 'HCP-DCR-2024-11-21-00-00-00.csv')

# 获取所有CSV文件的列表
csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

# 打开输出文件并写入数据
with open(output_file_path, 'w', newline='', encoding='utf-8') as output_file:
    writer = csv.writer(output_file)
    # 遍历所有CSV文件
    for filename in csv_files:
        # 打开每个CSV文件并读取数据
        with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            # 写入数据到输出文件
            for row in reader:
                writer.writerow(row)
