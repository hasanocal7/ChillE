from django.dispatch import receiver
from django.conf import settings
from django.db.models.signals import post_save
from django.contrib.auth.models import Group
from users.models import CustomUser

@receiver(post_save, sender=CustomUser)
def add_to_members_group(sender,instance,created,**kwargs):
    if created:
        group = Group.objects.get(name='Member')
        if instance.is_member:
           instance.groups.add(group)
