# Generated by Django 3.0.5 on 2020-04-23 19:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='tgMessage',
            fields=[
                ('message_id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='Message ID')),
                ('body', models.TextField(verbose_name='Message Text')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Send Date')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author')),
            ],
        ),
    ]
