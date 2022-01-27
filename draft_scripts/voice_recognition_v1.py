import torchaudio
from speechbrain.pretrained import EncoderClassifier
from speechbrain.pretrained import SpeakerRecognition

verification = SpeakerRecognition.from_hparams(source="speechbrain/spkrec-ecapa-voxceleb", savedir="pretrained_models/spkrec-ecapa-voxceleb")
signal,fs = torchaudio.load('./samples/audio_samples/ethan1.flac')
signal2,fs = torchaudio.load('./samples/audio_samples/a1.wav')
score, prediction = verification.verify_batch(signal, signal2)
print(score, prediction)