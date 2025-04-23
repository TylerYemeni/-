from faker import Faker

def generate_fake_identity():
    faker = Faker('ar_AA')
    identity = {
        "name": faker.name(),
        "email": faker.email(),
        "phone": faker.msisdn()[:10],
        "address": faker.address(),
        "username": faker.user_name()
    }
    return identity
