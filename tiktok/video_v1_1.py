import os
import random
import datetime
from moviepy.editor import VideoFileClip,TextClip, CompositeVideoClip, ImageClip, concatenate_videoclips
from moviepy.video.fx.all import speedx
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_audio

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
    # 获取原视频文件名（不包括扩展名）
    video_name = os.path.splitext(os.path.basename(video_path))[0]
    # 生成临时视频文件路径
    temp_cut_video_path = os.path.join(output_dir, f"cut_temp_video_{video_name}.mp4")
    # 保存裁剪后的视频
    cropped_video.write_videofile(temp_cut_video_path, codec='libx264')
    return temp_cut_video_path

# 视频变速功能
def change_video_speed(temp_cut_video_path,video_path, output_dir):
    # 加载视频
    video = VideoFileClip(temp_cut_video_path)
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
    speed_video = concatenate_videoclips([part1_speed, part2_speed, part3_speed])
    # 获取原视频文件名（不包括扩展名）
    video_name = os.path.splitext(os.path.basename(video_path))[0]
    # 生成临时视频文件路径
    temp_speed_video_path = os.path.join(output_dir, f"speed_temp_video_{video_name}.mp4")
    # 保存裁剪后的视频
    speed_video.write_videofile(temp_speed_video_path, codec='libx264')
    return temp_speed_video_path

# 视频静音
def mute_video(temp_speed_video_path,video_path, output_dir):
    # 加载视频
    video = VideoFileClip(temp_speed_video_path)
    # 对视频进行静音处理
    muted_video = video.without_audio()
    # 获取原视频文件名（不包括扩展名）
    video_name = os.path.splitext(os.path.basename(video_path))[0]
    # 生成临时视频文件路径
    temp_mute_video_path = os.path.join(output_dir, f"mute_temp_video_{video_name}.mp4")
    # 保存裁剪后的视频
    muted_video.write_videofile(temp_mute_video_path, codec='libx264')
    return temp_mute_video_path

# AI字幕
def extract_audio(video_path, audio_path):
    ffmpeg_extract_audio(video_path, audio_path)

    #定义transcribe_audio函数，接收音频路径和输出格式作为参数，使用OpenAI的API将音频转录为文本，并返回转录结果
def transcribe_audio(audio_path, output_format='verbose_json'):
    api_key = "sk-key"
    url = "https://api.openai.com/v1/audio/transcriptions"
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    files = {
        'file': open(audio_path, 'rb')
    }
    data = {
        'timestamp_granularities[]': 'word',
        'model': 'whisper-1',
        'response_format': output_format
    }
    response = requests.post(url, headers=headers, files=files, data=data)
    response_data = response.json()
    return response_data

    #定义add_subtitles_with_watermark函数，接收视频路径、字幕数据、输出路径、水印路径以及可选的填充参数，为视频添加字幕和水印，并输出处理后的视频
def add_subtitles_with_watermark(video_path, subtitles, output_path, watermark_path, top_padding=20, left_padding=20, text_padding=30):
    video = VideoFileClip(video_path)
    video = video.subclip(0, min(video.duration, subtitles[-1]['end_time']))

    # Create a list to hold TextClips
    text_clips = []

    # Define how many words you want to display per TextClip
    words_per_clip = 3

    # Group words into chunks
    for i in range(0, len(subtitles), words_per_clip):
        chunk = subtitles[i:i + words_per_clip]
        text = ' '.join(sub['text'] for sub in chunk).upper()  # Convert text to uppercase
        start_time = chunk[0]['start_time']
        end_time = chunk[-1]['end_time']

        # Create a TextClip for this chunk of words
        txt_clip = TextClip(text, fontsize=54, font='Arial-Bold', color='white', bg_color='black')
        # Adjust position to incorporate padding
        txt_clip = txt_clip.set_position(('center', 'center')).set_start(start_time).set_end(end_time)
        # Add padding to the text box
        txt_clip = txt_clip.margin(top=text_padding, bottom=text_padding, left=text_padding, right=text_padding, color=(0, 0, 0))
        text_clips.append(txt_clip)

    # Overlay the TextClips onto the video
    video_with_subtitles = CompositeVideoClip([video] + text_clips)

    # Load the watermark image
    watermark = ImageClip(watermark_path)
    watermark = watermark.set_duration(video.duration)
    watermark = watermark.set_opacity(1.0)  # Adjust opacity as needed

    # Calculate position for the watermark
    watermark_position = (left_padding, top_padding)

    # Add the watermark to the video
    video_with_watermark = CompositeVideoClip([video_with_subtitles.set_position('center'), watermark.set_position(watermark_position)])

    # Write the final video file
    video_with_watermark.write_videofile(output_path, codec="libx264", audio_codec="aac")


    #定义process_video_folder函数，遍历指定文件夹中的视频文件，提取音频、进行转录、添加字幕和水印，最后输出到指定的输出文件夹，并在完成后删除临时音频文件
def process_video_folder(input_dir, output_dir):
    for filename in os.listdir(input_dir):
        if filename.endswith(".mp4"):
            video_path = os.path.join(input_dir, filename)
            audio_path = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}.mp3")
            output_path = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}.mp4")
            
            watermark_path = "logo.png"
            top_padding = 40
            left_padding = 40

            # Extract audio from video
            extract_audio(video_path, audio_path)

            # Transcribe audio
            transcriptions = transcribe_audio(audio_path)

            # Extract transcriptions with timestamps
            subtitles = []
            for word in transcriptions['words']:
                subtitles.append({
                    'text': word['word'],
                    'start_time': word['start'],
                    'end_time': word['end']
                })

            # Add subtitles and watermark to video
            add_subtitles_with_watermark(video_path, subtitles, output_path, watermark_path, top_padding, left_padding)

            # Clean up temporary audio file
            os.remove(audio_path)

# 主函数更新
def main(input_dir, output_dir):
    # 确保输出目录存在
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 遍历指定目录下的所有.mp4和.mkv格式的视频文件
    for filename in os.listdir(input_dir):
        if filename.endswith(".mp4") or filename.endswith(".mkv"):
            video_path = os.path.join(input_dir, filename)
            # 裁剪视频
            temp_cut_video_path = crop_video(video_path, output_dir)
            # 变速处理
            temp_speed_video_path = change_video_speed(temp_cut_video_path,video_path, output_dir)
            # 删除临时裁剪视频文件
            os.remove(temp_cut_video_path)
            # 静音视频
            muted_video = mute_video(temp_speed_video_path,video_path, output_dir)
            # 删除临时变速视频文件
            #os.remove(temp_speed_video_path)
            # 结束处理
            # 获取原视频文件名（不包括扩展名）
            video_name = os.path.splitext(os.path.basename(video_path))[0]
            # 生成最终视频文件路径，包含完整日期和时间
            current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")
            final_video_path = os.path.join(output_dir, f"final_video_{video_name}_{current_time}.mp4")
            # 使用VideoFileClip对象保存视频
            muted_video.write_videofile(final_video_path, codec='libx264')
            return final_video_path
        

# 指定的输入和输出目录
input_dir = r"C:\Users\e0449219\AppData\Local\video_cut\sample_video"
output_dir = r"C:\Users\e0449219\AppData\Local\video_cut\output"

# 运行主函数
final_video_path = main(input_dir, output_dir)
process_video_folder(input_dir, output_dir)
print(f"最终视频已保存至: {final_video_path}")