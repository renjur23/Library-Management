# Generated by Django 5.0.6 on 2024-07-10 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('book_spec', models.CharField(max_length=255)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
