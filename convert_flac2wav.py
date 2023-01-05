import os
import soundfile as sf

save_path = "Data/human_records/full_records_wav/"
read_path = "Data/human_records/full_records_flac/"
for record in os.listdir(read_path):
    # audio = AudioSegment.from_file(read_path + record, format="flac")
    audio, rate = sf.read(read_path + record)
    sf.write(save_path + record[:-4] + "wav", audio, rate, format="wav")

