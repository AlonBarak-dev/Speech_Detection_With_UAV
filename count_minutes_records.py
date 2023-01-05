import os
from scipy.io import wavfile

seconds = 0

read_path = "Data/human_records/full_records_wav/"

for file in os.listdir(read_path):
    rate, data = wavfile.read(read_path + file)
    seconds += len(data)/rate

print("Homan records Data length is: {} minutes".format(seconds/60))