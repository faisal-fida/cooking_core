# Generated by Django 4.2 on 2023-05-16 01:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_comment_balance'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='balance',
            new_name='amount',
        ),
    ]
