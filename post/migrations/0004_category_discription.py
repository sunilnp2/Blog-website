# Generated by Django 4.1 on 2022-08-10 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='discription',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
