from django.db import models


class Person(models.Model):
    PERSON_TYPE = [('S', 'Student'), ('F', 'Faculty'), ('O', 'Other')]
    personid = models.AutoField(primary_key=True, default=999)
    firstname = models.CharField(max_length=20, default='firstname')
    middlename = models.CharField(max_length=10, default='middlename')
    lastname = models.CharField(max_length=30, default='lastname')
    userid = models.IntegerField(default=999)
    email = models.EmailField(max_length=50, default='emailfield')
    persontype = models.CharField(choices=PERSON_TYPE, max_length=1, blank=True)


class Reservation(models.Model):
    reservaionid = models.AutoField(primary_key=True, default=0)
    userid = models.IntegerField(default=999)
    reservation_name = models.CharField(max_length=50, default='reservation_name')

class User(models.Model):
    userid=models.IntegerField(default=999)
    reservation_made = models.ManyToManyField('Reservation', blank=False)


class Contact(models.Model):
    contact = models.CharField(max_length=50)


class UserCategory(models.Model):
    pass

class Room(models.Model):
    pass


class RoomCategory(models.Model):
    pass


class RoomStatus(models.Model):
    pass


class Equipment(models.Model):
    pass
