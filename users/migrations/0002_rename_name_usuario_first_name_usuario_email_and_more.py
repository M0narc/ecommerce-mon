# Generated by Django 4.2.6 on 2023-12-11 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='usuario',
            name='email',
            field=models.EmailField(max_length=100, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='last_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
