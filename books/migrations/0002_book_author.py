# Generated by Django 3.0.5 on 2020-04-27 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=128, null=True),
        ),
    ]