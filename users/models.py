from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', null=True, blank=True)
    is_verify = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'


class EmailVerification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.UUIDField(unique=True)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    expiration = models.DateTimeField()

    def __str__(self):
        return f'Подтверждение почты для {self.user.username}, email: {self.user.email}'

    def send_verification_email(self):
        send_mail(
            "Subject here",
            "Test verification.",
            "from@example.com",
            [self.user.email],
            fail_silently=False,
        )
