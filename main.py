from modules.logger.logger import setup_logger
from modules.vpn.auto_connect import connect_to_vpn
from modules.identity.generator import generate_fake_identity
from modules.voice.fake_voice import generate_voice
from modules.report.whatsapp_report import send_whatsapp_report

logger = setup_logger()

def main():
    logger.info("تشغيل أداة أبو سالم...")

    ip = connect_to_vpn()
    logger.info(f"تم الاتصال بـ VPN الوهمي: {ip}")

    identity = generate_fake_identity()
    logger.info(f"تم توليد هوية وهمية: {identity}")

    voice_file = generate_voice(identity)
    logger.info("تم توليد ملف صوتي وهمي.")

    result = send_whatsapp_report(identity, voice_file)
    if result:
        logger.info("تم إرسال البلاغ الحقيقي بنجاح.")
    else:
        logger.error("فشل إرسال البلاغ.")

if __name__ == "__main__":
    main()
