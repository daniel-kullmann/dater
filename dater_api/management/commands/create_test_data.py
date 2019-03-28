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
        {
            'username': 'u01',
            'e_mail': 'u01@examle.com',
            'phone_number': '+49-999-888-01'
        },
        {
            'username': 'u02',
            'e_mail': 'u02@examle.com',
            'phone_number': '+49-999-888-02'
        },
        {
            'username': 'u03',
            'e_mail': 'u03@examle.com',
            'phone_number': '+49-999-888-03'
        },
        {
            'username': 'u04',
            'e_mail': 'u04@examle.com',
            'phone_number': '+49-999-888-04'
        },
        {
            'username': 'u05',
            'e_mail': 'u05@examle.com',
            'phone_number': '+49-999-888-05'
        },
        {
            'username': 'u06',
            'e_mail': 'u06@examle.com',
            'phone_number': '+49-999-888-06'
        },
        {
            'username': 'u07',
            'e_mail': 'u07@examle.com',
            'phone_number': '+49-999-888-07'
        },
        {
            'username': 'u08',
            'e_mail': 'u08@examle.com',
            'phone_number': '+49-999-888-08'
        },

    ]

    def create_consumers(self):
        for user in Command.consumer_users:
            exists = User.objects.filter(username=user['username'])
            user_data = None
            if len(exists) == 0:
                user_data = User.objects.create_user(
                    username=user['username'],
                    password=user['username'],
                    email=user['e_mail'],
                    is_active=True
                )
            elif len(exists) == 1:
                user_data = exists[0]
            else:
                raise Exception("the user " + user['username'] + "exists multiple times")

            exists = ConsumerData.objects.filter(user_id=user_data.id)
            if len(exists) == 0:
                consumer_data = ConsumerData(user=user_data, phone_number=user['phone_number'])
                consumer_data.save()
            elif len(exists) == 1:
                consumer_data = exists[0]
                consumer_data.phone_number = user['phone_number']
                #consumer_data.session_key = user['session_key']
                consumer_data.save()
            else:
                raise Exception("the consumer data for " + user['username'] + "exists multiple times")

    def create_providers(self):
        for user in Command.provider_users:
            exists = User.objects.filter(username=user['username'])
            user_data = None
            if len(exists) == 0:
                user_data = User.objects.create_user(
                    username=user['username'],
                    password=user['username'],
                    is_active=True
                )
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
            else:
               client = exists[0]

            slot_types = SlotType.objects.filter(client=client)
            if len([slot_type for slot_type in slot_types if slot_type.name == '30 minutes']) == 0:
                SlotType(client=client, name='30 minutes', length=1800).save
            if len([slot_type for slot_type in slot_types if slot_type.name == '1 hour']) == 0:
                SlotType(client=client, name='1 hour', length=3600).save
            if len([slot_type for slot_type in slot_types if slot_type.name == '90 minutes']) == 0:
                SlotType(client=client, name='90 minutes', length=5400).save

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

    def handle(self, *args, **kwargs):
        self.create_providers()
        self.create_consumers()
        #self.create_slot_types()
        #self.create_available_slots()
        #self.create_booked_slots()
