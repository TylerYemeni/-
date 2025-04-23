def send_report(identity, voice_path):
    # محاكاة إرسال بلاغ باستخدام المعلومات المزيفة
    print(f"جارٍ إرسال بلاغ باسم: {identity['name']}")
    print(f"البريد: {identity['email']}")
    print(f"الصوت: {voice_path}")
    return True
