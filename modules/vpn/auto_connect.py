import random

def connect_to_vpn():
    fake_ip = f"10.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}"
    print(f"[VPN] تم الاتصال بعنوان IP وهمي جديد.")
    return fake_ip
