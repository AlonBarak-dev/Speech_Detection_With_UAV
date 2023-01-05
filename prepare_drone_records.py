import os
from scipy.io import wavfile

read_path = "Data/drone_records/"
save_path = "Data/drone_records_one_minute/record_"
file_counter = 0

for file_name in os.listdir(read_path):

    rate, data = wavfile.read(read_path + file_name)
    # if longer than 1 minute, divide to 2 files
    if len(data) / rate > 60:
        wavfile.write(save_path + str(file_counter) + ".wav", rate, data[:60*rate])
        print(save_path + str(file_counter) + ".wav")
        file_counter += 1
        wavfile.write(save_path + str(file_counter) + ".wav", rate, data[60*rate:])
        print(save_path + str(file_counter) + ".wav")
        file_counter += 1
    else:
        wavfile.write(save_path + str(file_counter) + ".wav", rate, data)
        print(save_path + str(file_counter) + ".wav")
        file_counter += 1

