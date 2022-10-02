#实现音频变调
from ffmpeg import audio
import subprocess
import os
audio_path = r'D:/file'
finish_path = r'D:/file/voice_output1.wav'

# 调整音频播放速率
def a_speed(input_file, speed, out_file):
    try:
        cmd = "ffmpeg -y -i %s -filter_complex \"atempo=tempo=%s\" %s" % (input_file, speed, out_file)
        res = subprocess.call(cmd, shell=True) 
        if res != 0:
            return False
        return True
    except Exception:
        return False

def run():
    audio_file = os.listdir(audio_path)
    for _, audio1 in enumerate(audio_file):
        print(audio_path+audio1)
        audio.a_speed(audio_path+audio1, "2", finish_path+"2x"+audio1)
run()