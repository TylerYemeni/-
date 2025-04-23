from gtts import gTTS

def generate_voice(identity, filename="voice.mp3"):
    text = f"مرحباً، اسمي {identity['name']}. أود الإبلاغ عن رقم مزعج."
    tts = gTTS(text=text, lang='ar')
    tts.save(filename)
    return filename
