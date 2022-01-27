import pyaudio, wave, os
from success_window import Ui_msg_success
from error_window import Ui_error_window
from PyQt5 import QtCore, QtGui, QtWidgets
from speechbrain.pretrained import EncoderClassifier
from speechbrain.pretrained import SpeakerRecognition
from audios_encryption import encrypt, decrypt

def showErrorMsg(wd, msg): #error in voice login/register
    wd.window = QtWidgets.QDialog()
    wd.ui = Ui_error_window()
    wd.ui.setupUi(wd.window)
    wd.window.show()
    wd.ui.error_msg.setText(msg)

def showSuccessMsg(wd,msg):  # registered/authenticated successfully
    wd.window = QtWidgets.QDialog()
    wd.ui = Ui_msg_success()
    wd.ui.setupUi(wd.window)
    wd.window.show()   
    wd.ui.register_success_msg.setText(msg)


def compare(username, wd):
    verification = SpeakerRecognition.from_hparams(source="pretrained_models/spkrec-ecapa-voxceleb", savedir="pretrained_models/spkrec-ecapa-voxceleb")
    f1 = './audios/'+username+'_regist.wav'
    f2 = './audios/'+username+'.wav'
    if os.path.exists(f1) and os.path.exists(f2):
        decrypt(username,username+'_regist')
        score, prediction = verification.verify_files(f1, f2)
        print(prediction.item())
        encrypt(username,username+'_regist')
        return prediction.item()
    showErrorMsg(wd, "Error while comparing voice regists.")

def audio(filename, username='', regist=False):
    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 1
    fs = 44100  # Record at 44100 samples per second
    seconds = 15

    p = pyaudio.PyAudio()  # Create an interface to PortAudio
    print('Recording')

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input_device_index=1,
                    input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)

    # Stop and close the stream 
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    print('Finished recording')

    # Save the recorded data as a WAV file
    wf = wave.open("./audios/"+filename+".wav", 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()

    if regist:
        encrypt(username,filename)