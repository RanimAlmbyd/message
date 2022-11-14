# Generated by Django 4.1.3 on 2022-11-14 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=20)),
                ('recipient', models.CharField(max_length=20)),
                ('send_date', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=20)),
                ('text', models.CharField(max_length=300)),
                ('read', models.BooleanField(default=False)),
            ],
        ),
    ]