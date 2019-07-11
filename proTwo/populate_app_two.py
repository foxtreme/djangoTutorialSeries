import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','proTwo.settings')
import django
django.setup()

from AppTwo.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):
    for entry in range(N):
        User.objects.get_or_create(first_name= fakegen.first_name(),
                                   last_name= fakegen.last_name(),
                                   email= fakegen.email())[0]

if __name__=="__main__":
    print('populating users...')
    populate(15)
    print('populating complete...')