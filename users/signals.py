from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.dispatch import receiver

from users.models import CustomUser


@receiver(post_save, sender=CustomUser)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        send_mail(
            f"You have been successfuly registered!",
            f"Salom {instance.username}\n\nGoodReadsga xush kelibsiz! Ro'yxatdan o'tish jarayonini muvoffaqiyatli tugallandi.\n\nAgar sizning boshqa savollar yoki takliflaringiz bo'lsa https://t.me/javohirtwits kanal izohlariga yozishingiz mumkin.\n\nYana bir bor bizni tanlaganingiz uchun rahmat!\n\nHurmat bilan,\n\n{instance.first_name}\n\nGoodReads Jamoasi\n\n",
            "coderjek@gmail.com",
            [instance.email],
        )
