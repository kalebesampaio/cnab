# Generated by Django 4.1.5 on 2023-01-26 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField()),
                ('date_and_hour', models.DateTimeField()),
                ('value', models.IntegerField()),
                ('cpf', models.IntegerField()),
                ('card', models.CharField(max_length=12)),
                ('owner', models.CharField(max_length=14)),
                ('name', models.CharField(max_length=19)),
            ],
        ),
    ]
