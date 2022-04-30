from django.db.models.signals import post_save
from.models import custom_user
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from.models import profile
@receiver(post_save,sender=custom_user)
def create_profile(sender,instance,created,**kwargs):
    if created:
        profile.objects.create(user=instance)

@receiver(post_save,sender=custom_user)
def save_profile(sender, instance , **kwargs):
        instance.profile.save()

@receiver(post_save, sender=custom_user)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)