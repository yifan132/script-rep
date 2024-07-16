import os
import random
import datetime
from moviepy.editor import VideoFileClip, concatenate_videoclips
from moviepy.video.fx.all import speedx


# 视频裁剪功能
def crop_video(video_path, output_dir):
    # 加载视频
    video = VideoFileClip(video_path)
    # 视频总时长
    duration = video.duration
    # 随机选择裁剪的起始时间，确保裁剪后的视频时长在25-35秒之间
    start_time = random.uniform(0, duration - 35)
    end_time = start_time + random.uniform(25, 35)
    # 裁剪视频
    cropped_video = video.subclip(start_time, end_time)
    # 生成临时视频文件路径
    temp_video_path = os.path.join(output_dir, "temp_video.mp4")
    # 保存裁剪后的视频
    cropped_video.write_videofile(temp_video_path, codec='libx264')
    return temp_video_path

# 视频变速功能
def change_video_speed(temp_video_path, output_dir):
    # 加载视频
    video = VideoFileClip(temp_video_path)
    # 视频总时长
    duration = video.duration
    # 将视频切分为等时长的三份
    part_duration = duration / 3
    part1 = video.subclip(0, part_duration)
    part2 = video.subclip(part_duration, 2 * part_duration)
    part3 = video.subclip(2 * part_duration, duration)
    
    # 分别对三个片段进行变速
    part1_speed = part1.fx(speedx, 0.8)
    part2_speed = part2.fx(speedx, 1.2)
    part3_speed = part3.fx(speedx, 0.8)
    
    # 合并变速后的视频片段
    final_video = concatenate_videoclips([part1_speed, part2_speed, part3_speed])
    # 生成最终视频文件路径
    current_time = datetime.datetime.now().strftime("%H%M%S")
    final_video_path = os.path.join(output_dir, f"final_video_{current_time}.mp4")
    # 保存最终视频
    final_video.write_videofile(final_video_path, codec='libx264')
    return final_video_path

# 主函数
def main(video_path, output_dir):
    # 确保输出目录存在
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 裁剪视频
    temp_video_path = crop_video(video_path, output_dir)
    
    # 变速处理
    final_video_path = change_video_speed(temp_video_path, output_dir)
    
    return final_video_path

# 视频路径和输出目录
video_path = r"C:\Users\yangy\Desktop\tiktok项目\video_cut\sample_video\test1.mp4"
output_dir = r"C:\Users\yangy\Desktop\tiktok项目\video_cut\output"

# 运行主函数
final_video_path = main(video_path, output_dir)
print(f"最终视频已保存至: {final_video_path}")
