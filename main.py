from modules.logger.logger import setup_logger
from modules.vpn.auto_connect import connect_to_fake_vpn
from modules.identity.fake_identity import generate_fake_identity
from modules.voice.fake_voice import generate_fake_voice
from modules.report.sender import send_fake_report

def main():
    # إعداد التسجيل
    logger = setup_logger()
    logger.info("تشغيل أداة أبو سالم...")

    # 1. الاتصال بـ VPN وهمي
    connect_to_fake_vpn()
    logger.info("تم الاتصال بـ VPN الوهمي.")

    # 2. توليد هوية وهمية
    identity = generate_fake_identity()
    logger.info(f"تم توليد هوية وهمية: {identity}")

    # 3. توليد صوت وهمي بالاسم
    generate_fake_voice(f"مرحباً، اسمي {identity['name']}", filename="voice.mp3")
    logger.info("تم توليد ملف صوتي وهمي.")

    # 4. تنفيذ بلاغ وهمي
    send_fake_report(identity)
    logger.info("تم إرسال البلاغ بنجاح.")

if __name__ == "__main__":
    main()
