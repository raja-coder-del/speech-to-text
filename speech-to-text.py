from IPython.display import Audio
from scipy.io import wavfile
import numpy as np
file_name="my audio.wav"
Audio(file_name)
data=wavfile.read(file_name)
framerate=data[0]
sounddata=data[1]
time=np.arange(0,len(sounddata))/framerate
print(framerate)
print('Total time:',len(sounddata)/framerate)
!pip install -q transformers
import soundfile as sf
import librosa
import torch
from transformers import Wav2Vec2ForCTC,Wav2Vec2Tokenizer
tokenizer=Wav2Vec2Tokenizer.from_pretrained("facebook/wav2vec2-base-960h")
model=Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")
input_audio, _=librosa.load(file_name,sr=17000)
input_values=tokenizer(input_audio,return_tensors="pt").input_values
logits=model(input_values).logits
predicted_ids=torch.argmax(logits,dim=-1)
transcription=tokenizer.batch_decode(predicted_ids)[0]
text=transcription
print(text)
-output-
HI EVERYONE IM RAJA THIS IS MY PYTHON PROGRAMME THAT CONVERTS SPEECH TO TEXT
