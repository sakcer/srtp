#实现音频文件加噪
import wave
import numpy as np
import matplotlib.pyplot as plt
f = wave.open(r'D:/file/voice_test.wav', "rb")
params = f.getparams()
nchannels, sampwidth, framerate, nframes = params[:4]
strData = f.readframes(nframes)#读取音频，字符串格式
waveData = np.fromstring(strData,dtype=np.int16)#将字符串转化为int
waveData = waveData*1.0/(max(abs(waveData)))#wave幅值归一化
waveData = np.reshape(waveData,[nframes,nchannels])
f.close()

f = wave.open(r'D:/file/voice_test1.wav', "rb")
params = f.getparams()
nchannels, sampwidth, framerate, nframes = params[:4]
strData = f.readframes(nframes)#读取音频，字符串格式
waveData = np.fromstring(strData,dtype=np.int16)#将字符串转化为int
waveData = waveData*1.0/(max(abs(waveData)))#wave幅值归一化
waveData = np.reshape(waveData,[nframes,nchannels]).T

g = wave.open(r'D:/file/voice_test2.wav', "rb")
params2 = g.getparams()
nchannels2, sampwidth2, framerate2, nframes2 = params2[:4]
strData2 = g.readframes(nframes2)#读取音频，字符串格式
waveData2 = np.frombuffer(strData2,dtype=np.int16)#将字符串转化为int
waveData2 = waveData2*1.0/(max(abs(waveData2)))#wave幅值归一化
waveData2 = np.reshape(waveData2,[nframes2,nchannels2]).T

new = np.zeros(shape=(4,nframes))
for i in range(4):
    # 对不同长度的音频用数据零对齐补位，保证纯净音频长度
    if nframes < nframes2:
        rwaveData = waveData[i]
        rwaveData2 = waveData2[:,0:nframes]
    elif nframes > nframes2:
        length = abs(nframes2 - nframes)
        temp_array = np.zeros(length, dtype=np.int16)
        rwaveData2 = np.concatenate((waveData2, temp_array))
        rwaveData = waveData[i]
    else:
        rwaveData = waveData[i]
        rwaveData2 = waveData2
        
    new_waveData = rwaveData + rwaveData2
    new[i] = new_waveData
f.close()
g.close()

plt.figure(1)
plt.subplot(2,2,1)
plt.plot(waveData[0])
plt.ylabel('Frequency(Hz)')
plt.xlabel('Time(s)')

plt.subplot(2,2,2)
plt.plot(waveData[1])
plt.ylabel('Frequency(Hz)')
plt.xlabel('Time(s)')

plt.subplot(2,2,3)
plt.plot(waveData[2])
plt.ylabel('Frequency(Hz)')
plt.xlabel('Time(s)')

plt.subplot(2,2,4)
plt.plot(waveData[3])
plt.ylabel('Frequency(Hz)')
plt.xlabel('Time(s)')


plt.figure(2)
plt.subplot(2,2,1)
plt.plot(new[0])
plt.ylabel('Frequency(Hz)')
plt.xlabel('Time(s)')

plt.subplot(2,2,2)
plt.plot(new[1])
plt.ylabel('Frequency(Hz)')
plt.xlabel('Time(s)')


plt.subplot(2,2,3)
plt.plot(new[2])
plt.ylabel('Frequency(Hz)')
plt.xlabel('Time(s)')


plt.subplot(2,2,4)
plt.plot(new[3])
plt.ylabel('Frequency(Hz)')
plt.xlabel('Time(s)')
plt.show()