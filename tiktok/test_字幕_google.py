import moviepy.editor as mp
import speech_recognition as sr
from moviepy.video.tools.subtitles import SubtitlesClip

# 定义一个视频剪辑类
class VideoEditor:
    def __init__(self, video_path, output_path):
        self.video_path = video_path
        self.output_path = output_path
        self.video = None
        self.subtitles = None

    # 从视频中提取音频
    def extract_audio(self):
        self.video = mp.VideoFileClip(self.video_path)
        audio_path = self.video_path.replace('.mp4', '.wav')
        self.video.audio.write_audiofile(audio_path, codec='pcm_s16le', bitrate='128k')
        return audio_path

    # 识别音频并生成字幕
    def recognize_speech(self, audio_path):
        recognizer = sr.Recognizer()
        with sr.AudioFile(audio_path) as source:
            audio = recognizer.record(source)
        # 使用Google Web Speech API进行语音识别
        text = recognizer.recognize_google(audio, language='zh-CN')
        print(text)
        # 这里只是一个示例，实际中你可能需要将文本转换为字幕格式
        subtitles = [(0, self.video.duration, text)]
        self.subtitles = SubtitlesClip(subtitles, font_size=20)

    # 将字幕增加到视频中
    def add_subtitles(self):
        if self.subtitles:
            final_video = mp.CompositeVideoClip([self.video, self.subtitles])
            final_video.write_videofile(self.output_path, codec='libx264', audio_codec='aac')

    # 执行视频剪辑的流程
    def process_video(self):
        audio_path = self.extract_audio()
        self.recognize_speech(audio_path)
        self.add_subtitles()
        print(f"视频已保存至: {self.output_path}")

# 使用示例
if __name__ == "__main__":
    # 视频路径和输出路径
    video_path = r"C:\Users\yangy\Desktop\tiktok\video_cut\sample_video\test.mp4"
    output_path = r"C:\Users\yangy\Desktop\tiktok\video_cut\output\test.mp4"

    # 创建视频剪辑对象
    editor = VideoEditor(video_path, output_path)

    # 开始处理视频
    editor.process_video()
