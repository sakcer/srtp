#实现音频文件加噪
import wave
import numpy as np

f = wave.open('', "rb")
params = f.getparams()
nchannels, sampwidth, framerate, nframes = params[:4]
strData = f.readframes(nframes)#读取音频，字符串格式
waveData = np.fromstring(strData,dtype=np.int16)#将字符串转化为int
waveData = waveData*1.0/(max(abs(waveData)))#wave幅值归一化
waveData = np.reshape(waveData,[nframes,nchannels])
f.close()
#加入指定信噪比的高斯白噪声
def awgn(x, snr, out='signal', method='vectorized', axis=0):
    # Signal power
    if method == 'vectorized':
        N = x.size
        Ps = np.sum(x ** 2 / N)
    elif method == 'max_en':
        N = x.shape[axis]
        Ps = np.max(np.sum(x ** 2 / N, axis=axis))
    elif method == 'axial':
        N = x.shape[axis]
        Ps = np.sum(x ** 2 / N, axis=axis)
    else:
        raise ValueError('method \"' + str(method) + '\" not recognized.')
    # Signal power, in dB
    Psdb = 10 * np.log10(Ps)
    # Noise level necessary
    Pn = Psdb - snr
    # Noise vector (or matrix)
    n = np.sqrt(10 ** (Pn / 10)) * np.random.normal(0, 1, x.shape)
    if out == 'signal':
        return x + n
    elif out == 'noise':
        return n
    elif out == 'both':
        return x + n, n
    else:
        return x + n

f = wave.open('', "rb")
params = f.getparams()
nchannels, sampwidth, framerate, nframes = params[:4]
strData = f.readframes(nframes)#读取音频，字符串格式
waveData = np.fromstring(strData,dtype=np.int16)#将字符串转化为int
waveData = waveData*1.0/(max(abs(waveData)))#wave幅值归一化
waveData = np.reshape(waveData,[nframes,nchannels]).T

g = wave.open('', "rb")
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
