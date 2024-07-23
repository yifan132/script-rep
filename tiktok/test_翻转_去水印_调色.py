import os
import datetime
from moviepy.editor import VideoFileClip, vfx

# 视频属性调整

#属性使用参考：https://zulko.github.io/moviepy/ref/videofx/moviepy.video.fx.all.blackwhite.html#moviepy.video.fx.all.blackwhite
'''color_temp: 色温调整。通常，色温值在 -1 到 1 之间，其中 0 表示无变化，负值使视频偏蓝（冷色调），正值使视频偏黄（暖色调）。
hue: 色调调整。色调值通常在 -0.5 到 0.5 之间，其中 0 表示无变化，负值使视频色调逆时针旋转，正值使视频色调顺时针旋转。
saturation: 饱和度调整。饱和度值在 0 到 2 之间，其中 1 表示原始饱和度，小于 1 的值降低饱和度，大于 1 的值增加饱和度。
brightness: 亮度调整。亮度值通常在 -1 到 1 之间，其中 0 表示无变化，负值使视频变暗，正值使视频变亮。
contrast: 对比度调整。对比度值在 0 到 2 之间，其中 1 表示原始对比度，小于 1 的值降低对比度，大于 1 的值增加对比度。
shadows: 阴影调整。阴影值通常在 -1 到 1 之间，其中 0 表示无变化，负值使阴影变暗，正值使阴影变亮。
sharpness: 锐度调整。锐度值通常在 -2 到 2 之间，其中 0 表示无变化，负值降低锐度，正值增加锐度。
grain: 颗粒调整。颗粒值通常在 0 到 1 之间，其中 0 表示无颗粒效果，值越大颗粒效果越明显。
RGB:降低图片的饱和度，使其黑白'''

def adjust_video_properties(
    video_path,
    output_dir,
    color_temp = 0.1, # 色温稍微偏暖
    hue = -0.1 ,      # 色调稍微逆时针旋转
    saturation = 1.2, # 饱和度增加
    brightness = 0.2, # 亮度增加
    contrast = 1.5,   # 对比度增加
    shadows = 0.1,    # 阴影稍微变亮
    sharpness = 0.5,  # 锐度增加
    grain = 0.05,      # 添加轻微颗粒效果
    RGB_R_value = 0.2125,
    RGB_G_value = 0.7154,
    RGB_B_value = 0.0721
    ):
    video = VideoFileClip(video_path)
    # 调整视频属性
    #色温调整
    if color_temp != 0 or hue != 0:
        video = video.fx(vfx.colorx, color_temp + hue)
    #黑白调整
        video = video.fx(vfx.blackwhite, RGB=[RGB_R_value, RGB_G_value, RGB_B_value], preserve_luminosity=False)
    #if saturation != 1: 
    #    video = video.fx(vfx.colorize, saturation)
    #if brightness != 0:
    #    video = video.fx(vfx.lum_contrast, brightness)
    #if contrast != 1:
    #    video = video.fx(vfx.contrast, contrast)

    #if shadows != 0:
    #    video = video.fx(vfx.brightness, shadows)
    #if sharpness != 0:
    #    video = video.fx(vfx.sharpness, sharpness)
    #if grain != 0:
    #    video = video.fx(vfx.add_grain, grain)
    
    # 保存调整后的视频
    video_name = os.path.splitext(os.path.basename(video_path))[0]
    adjusted_video_path = os.path.join(output_dir, f"adjusted_{video_name}.mp4")
    video.write_videofile(adjusted_video_path, codec='libx264')
    return adjusted_video_path

# 移除水印（示例）
def remove_watermark(video_path, output_dir):
    # 这里仅返回原视频路径，因为没有实现具体的水印去除逻辑
    # 实际应用中可能需要图像处理技术来定位和移除水印
    return video_path

# 水平翻转视频
def flip_video_horizontally(video_path, output_dir):
    video = VideoFileClip(video_path)
    flipped_video = video.fx(vfx.mirror_x)
    
    # 保存翻转后的视频
    video_name = os.path.splitext(os.path.basename(video_path))[0]
    flipped_video_path = os.path.join(output_dir, f"flipped_{video_name}.mp4")
    flipped_video.write_videofile(flipped_video_path, codec='libx264')
    return flipped_video_path

# 主函数
def main(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for filename in os.listdir(input_dir):
        if filename.endswith(('.mp4', '.mkv')):
            video_path = os.path.join(input_dir, filename)
            
            # 调整视频属性
            adjusted_video_path = adjust_video_properties(video_path, output_dir)
            
            # 移除水印
            no_watermark_video_path = remove_watermark(adjusted_video_path, output_dir)
            
            # 水平翻转视频
            final_video_path = flip_video_horizontally(no_watermark_video_path, output_dir)
            
            print(f"Processed video saved to: {final_video_path}")

# 请根据实际情况设置以下路径
input_dir = r"C:\Users\yangy\Desktop\tiktok\video_cut\sample_video"
output_dir = r"C:\Users\yangy\Desktop\tiktok\video_cut\output"

# 运行主函数
if __name__ == "__main__":
    main(input_dir, output_dir)
