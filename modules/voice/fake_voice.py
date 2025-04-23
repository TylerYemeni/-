from gtts import gTTS
import os

def generate_fake_voice(text, filename="output.mp3"):
    tts = gTTS(text=text, lang='ar')
    tts.save(filename)
    print(f"[Voice] تم توليد الصوت وحفظه في {filename}")
