# Generated by Django 3.2.11 on 2022-01-19 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learntech', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutoriallist',
            name='tutorialthmbnil',
            field=models.ImageField(default='', upload_to='learntech/image'),
        ),
    ]
