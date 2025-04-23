from gtts import gTTS
import os

def generate_fake_voice(name):
    text = f"مرحباً، اسمي {name} وأريد الإبلاغ عن مخالفة."
    tts = gTTS(text=text, lang='ar')
    voice_path = f"/root/voices/{name.replace(' ', '_')}.mp3"
    tts.save(voice_path)
    return voice_path
