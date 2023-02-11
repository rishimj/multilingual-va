from pydub import AudioSegment
import matplotlib.pyplot as plt
from scipy.io import wavfile
from tempfile import mktemp
from os import walk
import os
import numpy
from time import perf_counter

def get_files():
    input_dir = input("Enter the input directory: ")

    files = []
    os.chdir(input_dir)
    for (_, _, file_name) in walk(os.getcwd()):
        files.extend(file_name)

    return files, input_dir

def convert():
    files, input_dir = get_files()
    failed = 0
    counter = 0

    output_dir = input("Enter the output directory: ")
    if not os.path.exists("../" + output_dir):
        os.makedirs("../" + output_dir)

    for file in files:
        # +0
        if counter > 422:
            try: 
                audio = AudioSegment.from_file(file, format="m4a")
                wav = mktemp(".wav") 
                audio.export(wav, format="wav")
                rate, data = wavfile.read(wav)
                numpy.seterr(divide = 'ignore')
                plt.specgram(data, NFFT=128, Fs=rate, noverlap=0)
                plt.savefig("../" + output_dir + "/" + file[:-4] + ".png")
                counter += 1
            except: 
                print("FAILED")
                failed += 1
                counter += 1
        else: 
            counter += 1
    
    print(str(failed) + " FAILED")

convert()