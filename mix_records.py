import os
import random
from scipy.io import wavfile
import numpy as np
from pydub import AudioSegment

read_human_path = "Data/human_records/one_minute_records_wav/record_"
read_drone_path = "Data/drone_records_one_minute/"
save_path = "Data/mixed_records/record_"

file_counter = 0
num_of_mixed_records = 40
mixed_files = 0

for filename in os.listdir(read_drone_path):
    
    drone_sound = AudioSegment.from_wav(read_drone_path + filename)
    if mixed_files < num_of_mixed_records:
        human_sound = AudioSegment.from_wav(read_human_path + str(mixed_files) + ".wav")
        ratio = random.randint(-5, 5)
        drone_sound = drone_sound.overlay(human_sound, gain_during_overlay=ratio)
        mixed_files += 1

    drone_sound.export(save_path + str(file_counter) + ".wav", format='wav')
    file_counter += 1


        

