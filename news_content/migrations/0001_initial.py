# Generated by Django 3.2.6 on 2024-02-21 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('link', models.URLField()),
                ('pub_date', models.DateTimeField()),
                ('guid', models.CharField(max_length=100)),
                ('site_name', models.CharField(max_length=100)),
                ('site_logo', models.URLField(default=None)),
            ],
        ),
    ]