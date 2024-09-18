import os
import base64

# 配置路径
input_folder = r'C:\Users\yangy\Desktop\tiktok\头像\1'  # 输入文件夹路径
output_folder = r'C:\Users\yangy\Desktop\tiktok/头像_output'  # 输出文件夹路径
sql_file = r'C:\Users\yangy\Desktop\tiktok\头像_output/1.sql'  # SQL文件路径

# 确保输出文件夹存在
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 打开SQL文件
with open(sql_file, 'w', encoding='utf-8') as f:
    # 遍历所有子文件夹
    for subdir, dirs, files in os.walk(input_folder):
        for file in files:
            if file.lower().endswith(('.jpg','.png')):
                # 构建文件路径
                img_path = os.path.join(subdir, file)
                # 读取图片并转换为二进制
                with open(img_path, 'rb') as img_file:
                    img_binary = img_file.read()
                    img_base64 = base64.b64encode(img_binary).decode('utf-8')
                
                # 提取子文件夹名称和图片名称
                subdir_name = os.path.basename(subdir)
                img_name = os.path.splitext(file)[0]
                
                # 生成SQL语句
                sql_statement = f"update navy.user_baseinfo set head_portrait = '{img_base64}' where user_uid = {img_name}+9*10;\n"
                
                # 写入SQL文件
                f.write(sql_statement)

print('完成！')
