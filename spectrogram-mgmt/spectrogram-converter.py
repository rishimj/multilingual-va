from pydub import AudioSegment
import matplotlib.pyplot as plt
from scipy.io import wavfile
from tempfile import mktemp
from os import walk
import os
import numpy

def get_files():
    input_dir = input("Enter the input directory: ")

    files = []
    for (_, _, file_name) in walk(input_dir):
        files.extend(file_name)

    return files, input_dir

def convert():
    files, input_dir = get_files()

    output_dir = input("Enter the output directory: ")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir) 

    for file in files:
        audio = AudioSegment.from_file(input_dir + "/" + file, format="mp3")
        wav = mktemp(".wav") 
        audio.export(wav, format="wav")
        rate, data = wavfile.read(wav)
        numpy.seterr(divide = 'ignore') 
        plt.specgram(data, NFFT=128, Fs=rate, noverlap=0)
        plt.savefig(output_dir + "/" + file[:-4] + ".png")

convert()