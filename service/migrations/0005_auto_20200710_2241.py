# Generated by Django 2.2 on 2020-07-10 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_auto_20200710_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='writer',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]