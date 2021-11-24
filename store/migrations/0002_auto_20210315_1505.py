# Generated by Django 3.1.5 on 2021-03-15 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sporttype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('description', models.CharField(max_length=20)),
                ('pub_date', models.DateTimeField(verbose_name='Date published')),
            ],
        ),
        migrations.DeleteModel(
            name='Football',
        ),
    ]
