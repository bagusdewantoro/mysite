# Generated by Django 3.1.2 on 2020-11-01 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-terbit',)},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='created',
            new_name='dibuat',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='updated',
            new_name='diperbarui',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='judul',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='category',
            new_name='kategori',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='author',
            new_name='penulis',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='publish',
            new_name='terbit',
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=250, unique_for_date='terbit'),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('dimuat', 'Dimuat')], default='draft', max_length=10),
        ),
    ]
