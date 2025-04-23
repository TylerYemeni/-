from faker import Faker

fake = Faker()

def generate_fake_identity():
    return {
        "name": fake.name(),
        "email": fake.email(),
        "phone": fake.phone_number(),
        "address": fake.address()
    }
