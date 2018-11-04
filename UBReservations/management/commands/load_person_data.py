from csv import DictReader
from datetime import datetime

from django.core.management import BaseCommand

from UBReservations.models import Person, Reservation

from pytz import UTC


DATETIME_FORMAT = '%m/%d/%Y %H:%M'

RESERVATION_IDS = [
    '1231',
    '2345',
    '4545',
    '2245',
    '3564'
]

ALREADY_LOADED_ERROR_MESSAGE = """
If you need to reload the data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from person_data.csv into our Pet model"

    def handle(self, *args, **options):
        if Person.objects.exists() or Reservation.objects.exists():
            print('Person data already loaded...exiting.')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return
        print("Loading pet data for pets available for adoption")
        for row in DictReader(open('./person_data.csv')):
            person = Person()
            person.personid = row['personid']
            person.firstname = row['firstname']
            person.middlename = row['middlename']
            person.lastname = row['lastname']
            person.email = row['email']
            person.persontype = row['persontype']
            person.reservation = row['reservation']
            person.save()
