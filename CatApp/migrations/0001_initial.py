# Generated by Django 2.1.2 on 2018-10-03 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CatPicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField()),
                ('breed', models.CharField(blank=True, default='unknown', max_length=80)),
                ('cat_name', models.CharField(max_length=120)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
