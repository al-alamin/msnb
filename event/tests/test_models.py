from datetime import datetime

from django.contrib.auth.models import User
from django.test.testcases import TestCase
from django.utils.timezone import now

from event.models import Event, Registration


class TestModels(TestCase):
    def create_event(self):
        event = Event.objects.create(
            title='test event',
            start_time=now(),
            end_time=now(),
            registration_limit=20,
            fee=100
        )
        return event

    def create_registraion(self):
        event = self.create_event()
        user = User.objects.create_user('tareq', 'tareq@gmail.com', 'pass1234')
        reg = Registration.objects.create(
            event=event,
            attendee = user
        )
        return reg
    def test_create_event(self):
        new = self.create_event()
        self.assertTrue(isinstance(new,Event))
        print(new)

    def test_create_registraion(self):
        reg = self.create_registraion()
        self.assertTrue(reg)
        print(reg)
        available_seats = reg.event.available_seats
        self.assertEqual(available_seats,19)

