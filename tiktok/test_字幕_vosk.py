import moviepy.editor as mp
import vosk
from moviepy.video.VideoClip import TextClip
import json

# 定义一个视频剪辑类
class VideoEditor:
    def __init__(self, video_path, output_path, model_path):
        self.video_path = video_path
        self.output_path = output_path
        self.model_path = model_path
        self.video = None
        self.subtitles = None

    # 从视频中提取音频
    def extract_audio(self):
        self.video = mp.VideoFileClip(self.video_path)
        audio_path = self.video_path.replace('.mp4', '.wav')
        self.video.audio.write_audiofile(audio_path, codec='pcm_s16le', bitrate='128k')
        return audio_path

    # 使用vosk进行语音识别
    def recognize_speech(self, audio_path):
        model = vosk.Model(self.model_path)
        recognizer = vosk.KaldiRecognizer(model, 16000)
        with open(audio_path, 'rb') as audio_file:
            while True:
                data = audio_file.read(4000)
                if len(data) == 0:
                    break
                if recognizer.AcceptWaveform(data):
                    result = recognizer.Result()
                    # 将JSON结果字符串解析为字典
                    result_dict = json.loads(result)
                    # 提取文本
                    text = result_dict.get('text', '')
                    return text

    # 将字幕增加到视频中
    def add_subtitles(self, text):
        if text:
            # 创建一个文本剪辑
            text_clip = TextClip(text, fontsize=20, color='white')
            text_clip = text_clip.set_position(('center', 'bottom')).set_duration(self.video.duration)
            final_video = mp.CompositeVideoClip([self.video, text_clip])
            final_video.write_videofile(self.output_path, codec='libx264', audio_codec='aac')

    # 执行视频剪辑的流程
    def process_video(self):
        audio_path = self.extract_audio()
        text = self.recognize_speech(audio_path)
        self.add_subtitles(text)
        print(f"视频已保存至: {self.output_path}")

# 使用示例
if __name__ == "__main__":
    # 视频路径和输出路径
    video_path = r"C:\Users\e0449219\AppData\Local\video_cut\sample_video\test.mp4"
    output_path = r"C:\Users\e0449219\AppData\Local\video_cut\output\test.mp4"
    # vosk模型路径
    model_path = r"C:\Users\e0449219\AppData\Local\video_cut\vosk-model-small-cn-0.22"

    # 创建视频剪辑对象
    editor = VideoEditor(video_path, output_path, model_path)

    # 开始处理视频
    editor.process_video()
