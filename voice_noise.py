#实现音频文件加噪
import wave
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import sys
import os
import re

def add_noise(noisedir,cleandir,snr):
    # noisy
    splitdir=re.split(r"\\",noisedir)
    wavdir="" # 所有wav文件所在路径
    for i in range(len(splitdir) - 1):
        wavdir += splitdir[i] + '/'
    noisydir=wavdir+"noisy/"  # 带噪语音存储路径
    os.mkdir(noisydir)
    # noise
    for noisewav in os.listdir(noisedir):
        noise, fs = sf.read(noisedir+'/'+noisewav)
        noisy_splitdir=noisydir+"add_"+noisewav[:-4]+"/"
        os.mkdir(noisy_splitdir)
    # clean
        for cleanwav in os.listdir(cleandir):
            clean, Fs = sf.read(cleandir+"/"+cleanwav)
            # add noise
            if fs == Fs and len(clean) <= len(noise):
            	# 纯净语音能量
                cleanenergy = np.sum(np.power(clean,2))
                # 随机索引与clean长度相同的noise信号
                ind = np.random.randint(1, len(noise) - len(clean) + 1)
                noiselen=noise[ind:len(clean) + ind]
                # 噪声语音能量
                noiseenergy = np.sum(np.power(noiselen,2))
                # 噪声等级系数
                noiseratio = np.sqrt((cleanenergy / noiseenergy) / (np.power(10, snr * 0.1)))
                # 随机索引与clean长度相同的noise信号
                noisyAudio = clean + noise[ind:len(clean)+ind] * noiseratio
                # write wav
                noisywavname=noisy_splitdir+cleanwav[:-4]+"_"+noisewav[:-4]+"_snr"+str(snr)+".wav"
                sf.write(noisywavname, noisyAudio, 16000)
            else:
                print("fs of clean and noise is unequal or the length of clean is longer than noise's\n")
                sys.exit(-1)

noisedir=r"D:/file/noise"
cleandir=r"D:/file/clean"
snr=5
add_noise(noisedir,cleandir,snr)

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


