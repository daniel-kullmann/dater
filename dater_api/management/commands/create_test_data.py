from django.contrib.auth.models import User, Group
from django.core.management.base import BaseCommand, CommandError

from dater_api.models import *

class Command(BaseCommand):
    help = "adds some test data (users, available slots and booked slots)"

    provider_users = [
        {
            'username': 'p11',
            'client': 'c1'
        },
        {
            'username': 'p12',
            'client': 'c1'
        },
        {
            'username': 'p13',
            'client': 'c1'
        },
        {
            'username': 'p14',
            'client': 'c1'
        },
        {
            'username': 'p21',
            'client': 'c2'
        },
        {
            'username': 'p22',
            'client': 'c2'
        },
        {
            'username': 'p23',
            'client': 'c2'
        },
        {
            'username': 'p24',
            'client': 'c2'
        },
    ]

    consumer_users = [
    ]

    def create_consumers(self):
        pass

    def create_providers(self):
        for user in Command.provider_users:
            exists = User.objects.filter(username=user['username'])
            user_data = None
            if len(exists) == 0:
                user_data = User.objects.create_user(user['username'], user['username'], is_active=True)
            elif len(exists) == 1:
                user_data = exists[0]
            else:
                raise Exception("the user " + user['username'] + "exists multiple times")

            exists = ProviderClient.objects.filter(name=user['client'])
            if len(exists) == 0:
                client = ProviderClient(name=user['client'])
                client.save()
            elif len(exists) != 1:
                raise Exception("the client " + user['client'] + "exists multiple times")

            exists = ProviderData.objects.filter(user_id=user_data.id)
            if len(exists) == 0:
                provider_data = ProviderData(user=user_data, client=client)
                provider_data.save()
            elif len(exists) == 1:
                provider_data = exists[0]
                provider_data.client = client
                provider_data.save()
            else:
                raise Exception("the provider data for " + user['username'] + "exists multiple times")
        pass

    def handle(self, *args, **kwargs):
        self.create_providers()
        self.create_consumers()
        #self.create_slot_types()
        #self.create_available_slots()
        #self.create_booked_slots()
