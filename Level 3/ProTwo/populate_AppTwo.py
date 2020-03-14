import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","ProTwo.settings")

import django
django.setup()

import random
from faker import Faker
from AppTwo.models import User

fake_gen = Faker()

def populate(N=10):
    for entry in range(N):
        first_name = fake_gen.first_name()
        last_name = fake_gen.last_name()
        email = fake_gen.email()

        user = User.objects.get_or_create(first_name = first_name, last_name= last_name, email = email)

if __name__ == '__main__':
    populate(20)
