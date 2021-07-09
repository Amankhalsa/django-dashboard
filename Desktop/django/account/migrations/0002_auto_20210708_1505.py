# Generated by Django 3.2 on 2021-07-08 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')], max_length=250),
        ),
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.CharField(choices=[('STUDENTS', 'STUDENTS'), ('JUNIOR', 'JUNIOR'), ('MID', 'MID'), ('SENIOR', 'SENIOR')], max_length=250),
        ),
    ]