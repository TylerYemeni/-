import subprocess
import os
import random

def connect_vpn():
    profiles_dir = "/root/vpn_profiles"
    if not os.path.exists(profiles_dir):
        print("مجلد vpn_profiles غير موجود")
        return False

    profiles = [f for f in os.listdir(profiles_dir) if f.endswith(".ovpn")]
    if not profiles:
        print("لا يوجد ملفات VPN")
        return False

    selected = random.choice(profiles)
    profile_path = os.path.join(profiles_dir, selected)

    try:
        subprocess.Popen(["openvpn", "--config", profile_path])
        return True
    except Exception as e:
        print(f"خطأ أثناء تشغيل VPN: {e}")
        return False
