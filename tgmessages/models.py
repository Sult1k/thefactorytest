from django.db import models
from django.conf import settings


class tgMessage(models.Model):
    message_id = models.AutoField(verbose_name="Message ID", primary_key=True, auto_created=True, serialize=False)
    author_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Author ID")
    body = models.TextField(verbose_name="Message Text", null=False, blank=False)
    date_created = models.DateTimeField(verbose_name="Send Date", auto_now_add=True)

    def __str__(self):
        return self.body

# Create your models here.
