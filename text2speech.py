import torch
from TTS.api import TTS

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"

# List available 🐸TTS models
# print(TTS().list_models())

# Init TTS
tts = TTS("tts_models/en/ljspeech/tacotron2-DDC").to(device)

def generate_speech(script):
# Run TTS
# ❗ Since this model is multi-lingual voice cloning model, we must set the target speaker_wav and language
# Text to speech list of amplitude values as output
    wav = tts.tts_to_file(text=script, speaker_wav="my/cloning/audio.wav", file_path="/home/sachin/Desktop/hack/hackathon/script.wav")
# Text to speech to a file
# tts.tts_to_file(text="Hello world!", speaker_wav="my/cloning/audio.wav", language="en", file_path="output.wav")