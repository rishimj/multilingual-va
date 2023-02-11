from googletrans import Translator
import speech_recognition as sr

class VoiceAssistant:

    def __init__(self):
        self.mic = sr.Microphone()
        self.translator = Translator()
        self.en_rec = sr.Recognizer()
        self.te_rec = sr.Recognizer(language="te-IN")
        self.hi_rec = sr.Recognizer(language="hi-IN")
        self.active = False

    def standby(self):
        with self.mic as source:
            audio = self.en_rec.listen(source)
        
        self.active = self.recognizer.recognize_google(audio).lower() == "hey"

    def process_data(self, audio):
        pass 

    def evaluate_lang(self, spectrogram):
        pass

    def listen(self):
        with self.mic as source:
            if lang == "en":
                audio = self.en_rec.listen(source)
            elif lang == "te": 
                audio = self.te_rec.listen(source)
            else: 
                audio = self.te_rec.listen(source)
            
        print(self.recognizer.recognize_google(audio))

    def stt(self, speech, lang): 
        pass

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

    def tts(self, lang, text):
        pass

def main():
    va = VoiceAssistant()

    while True: 
        while not va.active:
            va.standby()

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

