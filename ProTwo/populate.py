import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()


import random
from AppTwo.models import User
from faker import Faker

fakegen = Faker()

def populate(N):

    for entry in range(N):

        fake_email = fakegen.email()
        fake_last_name = fakegen.last_name()
        fake_first_name = fakegen.first_name()


        us = User.objects.get_or_create(first_name=fake_first_name,last_name=fake_last_name,email=fake_email)[0]


if __name__ == '__main__':
    print("Populating script!")
    populate(10)
    print("Populating completed!")
