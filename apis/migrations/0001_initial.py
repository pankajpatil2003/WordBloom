# Generated by Django 4.2.4 on 2025-04-19 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='English',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang_code', models.CharField(max_length=10)),
                ('words', models.CharField(max_length=100)),
            ],
        ),
    ]
