# Generated by Django 2.2 on 2019-04-10 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='designation',
            field=models.CharField(default='General Admin', max_length=100),
        ),
    ]