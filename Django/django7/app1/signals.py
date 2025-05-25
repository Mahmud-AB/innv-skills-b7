from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import User

from app1.models import Student

@receiver(post_save, sender=User)
def create_student(instance, created, **kwargs):
    if created:
        Student.objects.create(user=instance)
        print("Student created")