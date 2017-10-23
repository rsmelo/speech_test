import wave
import subprocess
import pyaudio
import speech_recognition as sr

def say(text):
    subprocess.call('tts.exe -f 10 -v 1 "' + text + '"', shell=True)

def play_audio(filename):
    chunk = 1024
    wafe_file = wave.open(filename, "rb")
    player = pyaudio.PyAudio()

    stream = player.open(
        format=player.get_format_from_width(wafe_file.getsampwidth()),
        channels=wafe_file.getnchannels(),
        rate=wafe_file.getframerate(),
        output=True
    )

    data_stream = wafe_file.readframes(chunk)

    while data_stream:
        stream.write(data_stream)
        data_stream = wafe_file.readframes(chunk)

    stream.close()
    player.terminate()

def init_speech():
    recognizer = sr.Recognizer()
    print("listening...")
    play_audio("./audio/beep.wav")

    with sr.Microphone() as source:
        print("say something")
        audio = recognizer.listen(source)

    play_audio("./audio/beep.wav")
    command = ""
    try:
        command = recognizer.recognize_google(audio)
    except:
        print("Could not understand")

    print("Your command")
    print(command)
    say("You said: " + command)

init_speech()
