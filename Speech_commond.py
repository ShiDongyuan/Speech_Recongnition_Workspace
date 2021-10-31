import speech_recognition
print(speech_recognition.__version__)

import numpy as np 
from scipy.io.wavfile import read, write
import io

import matplotlib.pyplot as plt 

#------------------------------------------------------------------
def initiate_recognizer():
    initiate_recognizer = speech_recognition.Recognizer()
    #print(speech_recognition.Microphone.list_microphone_names())
    return initiate_recognizer

#------------------------------------------------------------------
def Record_voice_from_MIC(recoginizer):
    with speech_recognition.Microphone(device_index=1) as source:
        recoginizer.adjust_for_ambient_noise(source)
        print("===================================")
        print("开始录音")
        audio = recoginizer.listen(source)
        print("开始翻译")
        print("===================================")
        # a = audio.get_wav_data()
        # #testResult = struct.unpack('>HH', a)
        # rate, data = read(io.BytesIO(a))
        # print(data.shape)
        
        # plt.title('The response of the primary path')
        # plt.plot(data)
        # plt.ylabel('Amplitude')
        # plt.xlabel('Length (taps)')
        # plt.grid()
        # plt.show()
    
        return audio
#-----------------------------------------------------------------
def Drawing_wave_data(audio):
    a = audio.get_wav_data()
    rate, data = read(io.BytesIO(a))
    print(f'Sampling rate is : {rate}')
    Time_index= (1/rate)*np.array(list(range(data.shape[0])))
    
    plt.title('The raw data from the microphone')
    plt.plot(Time_index,data)
    plt.ylabel('Amplitude')
    plt.xlabel('Times (seconds)')
    plt.grid()
    plt.show()
    
#------------------------------------------------------------------        
def vorice_to_word(recoginizer,audio):

    try:
        word = recoginizer.recognize_google(audio,language="zh-CN")
    except:
        word = "错误"
    
    print("声音原文为： " + word)
    
    return word
#------------------------------------------------------------------
dic ={"开灯"        :   "指令1"
      , "关电视"    :   "指令2"
      , "开窗户"    :   "指令3"
      , "关掉空调"  :   "指令4"
      , "测试"      :   "指令5"
      , "错误"      :   "没录上音"}
def Phrase_word_for_commond(word):
    try:
        print("This is " + dic[word] + " !!!")
    except:
        print("不是指令")
        
def main():
    sr    = initiate_recognizer()
    audio = Record_voice_from_MIC(sr)
    Drawing_wave_data(audio)
    word  = vorice_to_word(sr,audio)
    Phrase_word_for_commond(word)
    
if __name__=="__main__":
    main()
    