from modules.logger.logger import setup_logger
from modules.vpn.auto_connect import connect_vpn
from modules.identity.fake_identity import generate_fake_identity
from modules.voice.fake_voice import generate_fake_voice
from modules.report.sender import send_report

logger = setup_logger()

def main():
    logger.info("بدء تشغيل أداة أبو سالم...")

    identity = generate_fake_identity()
    logger.info(f"هوية وهمية تم توليدها: {identity['name']} - {identity['email']}")

    vpn_connected = connect_vpn()
    if not vpn_connected:
        logger.error("فشل الاتصال بـ VPN")
        return

    voice_path = generate_fake_voice(identity['name'])
    logger.info(f"تم توليد صوت وهمي: {voice_path}")

    success = send_report(identity, voice_path)
    if success:
        logger.info("تم إرسال البلاغ بنجاح")
    else:
        logger.error("فشل في إرسال البلاغ")

if __name__ == "__main__":
    main()
