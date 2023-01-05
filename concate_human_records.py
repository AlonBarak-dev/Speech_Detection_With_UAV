import os
from scipy.io import wavfile
import numpy as np


file_counter = 0
read_path = "Data/human_records/full_records_wav/"
save_path = "Data/human_records/one_minute_records_wav/record_"

one_minute_data = []
rate = 16000

for file_name in os.listdir(read_path):

    # if the concate records reached 1 minute, save exactly 1 minute & reset
    if len(one_minute_data) / rate >= 60:
        wavfile.write(save_path + str(file_counter) + ".wav", rate, np.array(one_minute_data[: 60*rate]))
        one_minute_data = []
        file_counter += 1
        print(save_path + str(file_counter) + ".wav")
    else:
        # else, add another record
        rt, data = wavfile.read(read_path + file_name)
        one_minute_data.extend(data)