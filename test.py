from src.utils import audio
audio_file = 'answer.wav'
wav = audio.load_wav(audio_file, 16000)
print(wav)