# Generated by Django 3.0.3 on 2020-05-17 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_label', models.CharField(max_length=200)),
                ('tags', models.CharField(max_length=200)),
                ('last_done', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
