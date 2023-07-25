# Generated by Django 4.2.3 on 2023-07-22 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='gym',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('categories', models.CharField(max_length=50)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=1)),
                ('date_added', models.DateField(verbose_name='date_published')),
                ('promotion', models.BooleanField(default=False)),
            ],
        ),
    ]
