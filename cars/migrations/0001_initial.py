# Generated by Django 2.2.6 on 2020-09-05 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producer', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=5)),
                ('prod_year', models.IntegerField()),
                ('transmission', models.SmallIntegerField()),
                ('color', models.TextField()),
                ('producer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cars.Producer')),
            ],
        ),
    ]
