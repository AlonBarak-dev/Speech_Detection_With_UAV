import os
import random
from scipy.io import wavfile
import numpy as np
from pydub import AudioSegment

read_human_path = "Data/human_records/one_minute_records_wav/record_"
read_drone_path = "Data/drone_records_one_minute/"
save_path = "Data/mixed_records/record_"
label_path = "Data/labels/label_"

file_counter = 0
num_of_mixed_records = 40
mixed_files = 0

for filename in os.listdir(read_drone_path):
    mixed = False
    drone_sound = AudioSegment.from_wav(read_drone_path + filename)
    prob = random.randint(1, 10)
    if mixed_files < num_of_mixed_records and prob <= 3:
        human_sound = AudioSegment.from_wav(read_human_path + str(mixed_files) + ".wav")
        ratio = random.randint(-5, 5)
        drone_sound = drone_sound.overlay(human_sound, gain_during_overlay=ratio)
        mixed_files += 1
        mixed = True

    drone_sound.export(save_path + str(file_counter) + ".wav", format='wav')

    # label 1 if speech is included in the record, 0 else.
    with open(label_path + str(file_counter) + ".txt", 'w') as f:
        if mixed:
            f.write(str(1))
        else:
            f.write(str(0))

    file_counter += 1
    
print(mixed_files)

