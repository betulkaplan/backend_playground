# Generated by Django 4.0.2 on 2022-02-23 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_mytestjs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('ip', models.CharField(max_length=50)),
                ('registry_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='MyTestJS',
        ),
        migrations.DeleteModel(
            name='TestJS',
        ),
    ]