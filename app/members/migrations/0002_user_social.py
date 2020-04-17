# Generated by Django 2.2.10 on 2020-04-07 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='social',
            field=models.CharField(choices=[('L', 'local'), ('K', 'kakao'), ('D', 'discord'), ('GG', 'google'), ('GH', 'github')], default='L', max_length=2),
        ),
    ]