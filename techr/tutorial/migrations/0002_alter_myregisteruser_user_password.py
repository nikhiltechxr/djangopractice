# Generated by Django 3.2.11 on 2022-01-27 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myregisteruser',
            name='user_password',
            field=models.CharField(blank=b'I01\n', max_length=10, null=True),
        ),
    ]
