# Generated by Django 3.1.2 on 2020-11-01 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='Kehidupan', max_length=20),
        ),
    ]
