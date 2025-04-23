from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def send_whatsapp_report(identity, voice_file_path):
    try:
        print("[Report] فتح المتصفح...")
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        driver = webdriver.Chrome(options=options)

        # توجه إلى صفحة التبليغ الرسمية لواتساب
        driver.get("https://www.whatsapp.com/contact/nstagram")

        time.sleep(2)

        print("[Report] ملء نموذج التبليغ...")

        # مثال تعبئة حقول (حسب ما يظهر من نموذج واتساب)
        driver.find_element(By.NAME, "name").send_keys(identity['name'])
        driver.find_element(By.NAME, "email").send_keys(identity['email'])
        driver.find_element(By.NAME, "phone").send_keys(identity['phone'])
        driver.find_element(By.NAME, "message").send_keys(
            f"هذا الرقم ينتحل هويتنا، يرجى اتخاذ إجراء ضده. الاسم: {identity['name']}، العنوان: {identity['address']}")

        # إرسال النموذج
        driver.find_element(By.XPATH, '//button[text()="إرسال"]').click()

        time.sleep(2)
        driver.quit()

        print("[Report] تم إرسال البلاغ بنجاح.")
        return True

    except Exception as e:
        print(f"[Report] فشل إرسال البلاغ: {e}")
        return False
