from googletrans import Translator
import speech_recognition as sr
from speech_recognition import UnknownValueError
#from beepy import beep
import threading
from gtts import gTTS
from pygame import mixer
import time
from pydub import AudioSegment
import matplotlib.pyplot as plt
from scipy.io import wavfile
import numpy
import webview

class VoiceAssistant:

    def __init__(self):
        self.mic = sr.Microphone()
        self.translator = Translator()
        self.recognizer = sr.Recognizer()
        self.active = False

    def standby(self):
        with self.mic as source:
            audio = self.recognizer.listen(source)

        try: 
            self.active = "hello" in self.recognizer.recognize_google(audio).lower()
        except UnknownValueError as e: 
            pass
        
        #if self.active:
         #   ping = threading.Thread(target=beep, args=(5,))
          #  ping.start()

    def listen(self):
        with self.mic as source:
            audio = self.recognizer.listen(source)
            
            with open("temp/input.wav", "wb") as file:
                file.write(audio.get_wav())

        #ping = threading.Thread(target=beep, args=(5,))
        #ping.start()

        return audio

    def process_data(self, audio):
        audio = AudioSegment.from_file("temp/input.wav", format="wav")
        rate, data = wavfile.read(audio)
        numpy.seterr(divide = 'ignore') 
        plt.specgram(data, NFFT=128, Fs=rate, noverlap=0)
        plt.savefig("temp/spectrogram.png")

    def evaluate_lang(self, spectrogram):
        pass
        #pass through model

    def stt(self, audio, lang): 
        if lang == "en":
            speech = self.recognizer.recognize_google(audio)
        elif lang == "te": 
            speech = self.recognizer.recognize_google(audio, language="te-IN")
        else: 
            speech = self.recognizer.recognize_google(audio, language="hi-IN")

        return audio

    def te_to_en(self, text): 
        return self.translator.translate(text, src="te", dest="en")

    def en_to_te(self, text):
        return self.translator.translate(text, src="en", dest="te")

    def hi_to_en(self, text):
        return self.translator.translate(text, src="hi", dest="en")

    def en_to_hi(self, text):
        return self.translator.translate(text, src="en", dest="hi")

    def query(self, text):
        pass
        #pass query to open-source voice assitant

    def tts(self, lang, text):
        tts = gTTS(text, lang=lang, slow=False)
        tts.save("temp/output.mp3")

        mixer.init()
        mixer.music.load("temp/output.mp3")
        mixer.music.play()
        while mixer.music.get_busy():
            time.sleep(1)

def main():
    va = VoiceAssistant()

    window = webview.create_window("iVue RoboControl", 'ui.html',
                      js_api = va, width = int((width + 30) * 0.12), height = height,
                      x = -18, y = 0, resizable = False, fullscreen = False,
                      hidden = False, frameless = False, minimized = False, on_top = False,
                      confirm_close = True, text_select = False)
    webview.start(http_server=True)

    va = VoiceAssistant()
    print("starting...")

    while True: 
        while not va.active:
            va.standby()

        print("activated")
        audio = va.listen()
        processed = va.process_data(audio)
        lang = va.evaluate_lang(processed)
        speech = va.stt(audio, lang)

        if lang == "te": 
            speech = va.te_to_en(speech)
        elif lang == "hi":
            speech = va.hi_to_en(speech)

        response = va.query(speech)

        if lang == "te": 
            response = va.en_to_te(response)
        elif lang == "hi":
            response = va.en_to_hi(response)

        va.tts(lang, response)

        va.active = False

if __name__ == "__main__":
    main()
