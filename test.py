from scipy.io import wavfile
import numpy
from speechbrain.pretrained import SepformerSeparation as separator
import torchaudio
from pydub import AudioSegment
from time import sleep

sound1 = AudioSegment.from_file("Data/testwav.wav")
sound2 = AudioSegment.from_file("Data/record_102.wav")

combined = sound1.overlay(sound2, gain_during_overlay=-3)
combined.export("combined.wav", format='wav')

sleep(2)
print("loading model")

model = separator.from_hparams(source="speechbrain/sepformer-wsj02mix", savedir='pretrained_models/sepformer-wsj02mix')

source = model.separate_file(path='combined.wav')

torchaudio.save("source1hat.wav", source[:, :, 0].detach().cpu(), 16000)
torchaudio.save("source2hat.wav", source[:, :, 1].detach().cpu(), 16000)

