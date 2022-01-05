from django.core.management.base import BaseCommand
from faker import Faker
import random
from ...models import Owner, Workstation


class Command(BaseCommand):
    help = "Add data to the database"

    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(10):
            name = fake.name()
            dept = fake.company()
            phone = fake.phone_number()
            serial_number = fake.msisdn()
            owner_count = Owner.objects.count()
            owner = Owner.objects.get(pk=int(random.randint(1, owner_count)))
            Owner.objects.get_or_create(name=name, dept=dept, phone=phone)
            Workstation.objects.get_or_create(serial_number=serial_number, owner=owner)
            self.stdout.write(self.style.SUCCESS(f"{name} - {dept} - {phone} added"))
            
