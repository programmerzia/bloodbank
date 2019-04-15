# Generated by Django 2.2 on 2019-04-15 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.BooleanField(blank=True, default=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option_name', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.BooleanField(blank=True, default=True, null=True)),
                ('option_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='option_list', to='master_data.Option')),
            ],
        ),
    ]