# Generated by Django 2.2.1 on 2019-06-10 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0002_auto_20190609_0156'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='answer',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='registration',
            name='ques',
            field=models.CharField(choices=[('book', 'What Is your favorite book?'), ('food', 'What is your favorite food?'), ('city', 'What city were you born in?'), ('place', 'Where is your favorite place to vacation?')], default='book', max_length=10),
        ),
    ]