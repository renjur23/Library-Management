# Generated by Django 5.0.6 on 2024-07-14 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_rename_user_newuser_book_slug_alter_book_book_cat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='book_spec',
        ),
        migrations.AlterField(
            model_name='book',
            name='rating',
            field=models.FloatField(default=1, max_length=5),
        ),
    ]
