# Generated by Django 4.2 on 2023-05-16 02:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0004_alter_comment_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='amount',
            field=models.PositiveBigIntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
